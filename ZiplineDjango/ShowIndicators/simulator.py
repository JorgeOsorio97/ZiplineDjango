import pandas as pd
import numpy as np



class Simulator:
    #Constructor donde se toman los siguientes parametros:

    ##security:s
    ###Tipo Pandas.DataFrame debe tener OHLC 
    
    ##init_capital:(opcional)
    ###Tipo entero, el capital inicial de la simulacion 
    ###Si no se declara sera igual a std_purchase * costo de la accion en el dia 0
    
    ##std_purchase:(opcional)
    ###Acciones a comprar o vender cuando haya cambios
    ###Si no se declara es igual init_capital / costo de la accion en el dia 0
    def __init__(self, security, init_capital = None, std_purchase = None):
        self.security = security

        if init_capital is not None and std_purchase is not None:
            self.init_capital = init_capital
            self.std_purchase = std_purchase
        elif init_capital is not None:
            self.init_capital = init_capital
            self.std_purchase = None
        elif std_purchase is not None:
            self.init_capital = None
            self.std_purchase = std_purchase

    final_capital = 0
    indicators_names = []
    final_decision = []
    operations_made = 0
    shares_own = 0
    highest_point = 0
    lowest_point = 0 
    security_highest_point = 0
    security_lowest_point = 0 

    def check_first_purchase_method(self):
        if self.init_capital is not None and self.std_purchase is not None:
            if self.security['Close'].iloc[0] * self.std_purchase < self.init_capital:
                return "std_purchase"
            else:
                return "init_capital"
        elif self.init_capital is not None:
            return "init_capital"
        elif self.std_purchase is not None:
            return "std_purchase"

    def add_indicator(self, name:str, decision = {}):
        if len(self.security['Close']) == len(decision['decision']) and len(self.security['Close']) == len(decision['data']):
            self.security[name + "_decision"] = decision['decision']
            self.security[name + "_data"] = decision['data']
            self.indicators_names.append(name)
        else:
            print('el tamaño de tu decision es incorrecto')

    def calcDecision(self):
        if len(self.indicators_names)==0:
            return("Debes cargar los indicadores primero")
        for day in self.security.index.values:
            decision = pd.Series([])
            for indicator in self.indicators_names:
                decision = decision.append(pd.Series(self.security[indicator].loc[day]), ignore_index=True)
            decision.dropna()
            if len(decision) == 0:
                self.final_decision.append(None)
            else:
                sell_count = len(decision[decision == "Sell"])
                buy_count = len(decision[decision == "Buy"])
                if sell_count > buy_count:
                    self.final_decision.append('Sell')
                elif sell_count < buy_count:
                    self.final_decision.append('Buy')
                elif sell_count == buy_count:
                    self.final_decision.append(self.final_decision[-1])
        self.security['FinalDecision'] = self.final_decision
            
    
    def calc_earning(self):
        self.calcDecision()
        first_purchase_method = self.check_first_purchase_method()
        for i in np.arange(len(self.security['Close'])):
            if self.security['FinalDecision'].iloc[i] == None:
                pass
            elif self.security['FinalDecision'].iloc[i] == 'Buy':
                if  self.security['FinalDecision'].iloc[i-1] == 'Buy':
                    pass
                else:
                    if self.operations_made == 0:
                        if first_purchase_method == 'init_capital':
                            self.shares_own = int((self.init_capital / self.security['Close'].iloc[i]))
                            self.operations_made += 1
                        elif first_purchase_method == 'std_purchase':
                            self.shares_own = self.std_purchase
                            self.operations_made += 1   
                    else:
                        self.shares_own = int(self.final_capital/ self.security['Close'].iloc[i])
                        self.final_capital = self.  final_capital % self.security['Close'].iloc[i]
                    #print(self.shares_own)
                        
            elif self.security['FinalDecision'].iloc[i] == 'Sell':
                if  self.security['FinalDecision'].iloc[i-1] == 'Sell':
                    pass
                else:
                    if self.operations_made == 0:
                        pass
                    else:
                        self.final_capital += self.shares_own * self.security['Close'].iloc[i]
                        self.shares_own = 0
                        self.operations_made +=1    
            #Checar si es el momento mas alto o bajo de ganancias
            if self.shares_own == 0:
                if self.highest_point == None or self.highest_point < self.final_capital:
                    self.highest_point = self.final_capital
                if (self.lowest_point == None or self.lowest_point > self.final_capital or self.lowest_point == 0):
                    self.lowest_point = self.final_capital
            else:
                if self.highest_point == None or self.highest_point < (self.shares_own * self.security['Close'].iloc[i]):
                    self.highest_point = self.final_capital
                if (self.lowest_point == None or self.lowest_point > (self.shares_own * self.security['Close'].iloc[i]) or self.lowest_point == 0):
                    self.lowest_point = self.final_capital 