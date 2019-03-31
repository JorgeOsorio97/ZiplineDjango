from enum import Enum, auto
import pandas as pd
import numpy as np


# pylint: disable=line-too-long
class Simulator:

    #Class variables
    security = None
    export_results = False
    indicators_names = []

    #Trained Variables
    buys_made = 0
    sells_made = 0
    shares_own = 0
    highest_point = 0
    lowest_point = 0
    security_highest_point = 0
    security_lowest_point = 0
    real_init_capital = 0
    real_final_capital = 0
    diference_percentage = 0
    last_decision = ""
    #Working Varialbes
    init_date = ""
    end_date = ""
    final_capital = 0

    def __init__(self, security, init_capital=None, stock_quantity=None, export_results=False):
        """
        Parameters:
        -----------
        security: Pandas.DataFrame
            Datos tipo OHLC
        (init_capital):int, optional
            El capital inicial de la simulacion
            Si no se declara sera igual a stock_quantity * costo de la accion en el dia 0
        (stock_quantity): int, optional
            Acciones a comprar o vender cuando haya cambios
            Si no se declara es igual init_capital / costo de la accion en el dia 0
        """

        self.security = security

        if init_capital is not None and stock_quantity is not None:
            self.init_capital = init_capital
            self.stock_quantity = stock_quantity
        elif init_capital is not None:
            self.init_capital = init_capital
            self.stock_quantity = None
        elif stock_quantity is not None:
            self.init_capital = None
            self.stock_quantity = stock_quantity
        
        if export_results:
            self.export_results = True
        if len(self.indicators_names) is not 0:
            self.cleanSimulator()

    def check_first_purchase_method(self):
        if self.init_capital is not None and self.stock_quantity is not None:
            if self.security['Close'].iloc[0] * self.stock_quantity < self.init_capital:
                self.real_init_capital = self.security['Close'].iloc[0] * self.stock_quantity
                return FirstTransactionType.STOCK_QUANTITY
            else:
                self.real_init_capital = self.init_capital
                return FirstTransactionType.INIT_CAPITAL
        elif self.init_capital is not None:
            self.real_init_capital = self.init_capital
            return FirstTransactionType.INIT_CAPITAL
        elif self.stock_quantity is not None:
            self.real_init_capital = self.security['Close'].iloc[0] * self.stock_quantity
            return FirstTransactionType.STOCK_QUANTITY

    def calcRealFinalCapital(self):
        self.real_final_capital = (self.security['Close'].iloc[-1] * self.shares_own) + self.final_capital
        self.init_date = self.security.index.values[0]
        self.end_date = self.security.index.values[-1]
    
    def calcDiferencePercentage(self):
        self.diference_percentage = self.real_final_capital / self.real_init_capital

    def add_indicator(self, name, decision={}):
        if len(self.security['Close']) == len(decision['decision']) and len(self.security['Close']) == len(decision['data']):
            #print(name)
            self.security[name + "_decision"] = decision['decision']
            self.security[name + "_data"] = decision['data']
            self.indicators_names.append(name)
        else:
            print('el tamano de tu decision es incorrecto'.encode('utf-8'))

    def calcDecision(self):
        """
        Crear Columna con la decision diaria de acuerdo a la decision individual de los indicadores
        """
        final_decision = []
        #print(self.security.columns.values)
        #print(self.indicators_names)
        if not self.indicators_names: #Checks if empty
            print("Debes cargar los indicadores primero".encode('utf-8'))
        for day in self.security.index.values:
            decision = pd.Series([])
            for indicator in self.indicators_names:
                decision = decision.append(pd.Series(self.security[indicator+'_decision'].loc[day]), ignore_index=True)
            decision.dropna()
            if not decision:
                final_decision.append(None)
            else:
                sell_count = len(decision[decision == TransactionType.SELL])
                buy_count = len(decision[decision == TransactionType.BUY])
                if sell_count > buy_count:
                    final_decision.append(TransactionType.SELL)
                elif sell_count < buy_count:
                    final_decision.append(TransactionType.BUY)
                elif sell_count == buy_count:
                    final_decision.append(final_decision[-1])
        self.security['FinalDecision'] = final_decision
        self.last_decision = self.security['FinalDecision'].iloc[-1]


    def calc_earning(self, data = None):
        """
        Calcular las ganancias siguiendo la decision de compra durante todo el periodo de los datos
        """
        if data is None:
            data = self.security
        self.calcDecision()
        first_purchase_method = self.check_first_purchase_method()
        for i in np.arange(len(data['Close'])):
            if data['FinalDecision'].iloc[i] is None:
                pass
            elif data['FinalDecision'].iloc[i] == TransactionType.BUY:
                if  data['FinalDecision'].iloc[i-1] == TransactionType.BUY:
                    pass
                else:
                    if (self.buys_made + self.sells_made) == 0:
                        if first_purchase_method == FirstTransactionType.INIT_CAPITAL:
                            self.shares_own = int((self.init_capital/data['Close'].iloc[i]))
                            self.buys_made += 1
                        elif first_purchase_method == FirstTransactionType.STOCK_QUANTITY:
                            self.shares_own = self.stock_quantity
                            self.buys_made += 1
                    else:
                        self.shares_own = int(self.final_capital/ data['Close'].iloc[i])
                        self.final_capital = self.  final_capital % data['Close'].iloc[i]
                    #print(self.shares_own)

            elif data['FinalDecision'].iloc[i] == TransactionType.SELL:
                if  data['FinalDecision'].iloc[i-1] == TransactionType.SELL:
                    pass
                else:
                    if (self.buys_made + self.sells_made) == 0:
                        pass
                    else:
                        self.final_capital += self.shares_own * data['Close'].iloc[i]
                        self.shares_own = 0
                        self.sells_made +=1
            #Checar si es el momento mas alto o bajo de ganancias
            if self.shares_own == 0:
                if (self.highest_point is None
                        or self.highest_point < self.final_capital):
                    self.highest_point = self.final_capital
                if (self.lowest_point is None
                        or self.lowest_point > self.final_capital
                        or self.lowest_point == 0):
                    self.lowest_point = self.final_capital
            else:
                if (self.highest_point is None
                        or self.highest_point < (self.shares_own * data['Close'].iloc[i])):
                    self.highest_point = self.final_capital
                if (self.lowest_point is None
                        or self.lowest_point > (self.shares_own * data['Close'].iloc[i])
                        or self.lowest_point == 0):
                    self.lowest_point = self.final_capital
        self.calcRealFinalCapital()
        self.calcDiferencePercentage()

    def cleanSimulator(self):
        """
        Funcion para reiniciar el simulador y no usar valores en memoria
        """
        self.final_capital = 0
        self.indicators_names = []
        self.buys_made = 0
        self.sells_made = 0
        self.shares_own = 0 
        self.highest_point = 0
        self.lowest_point = 0
        self.security_highest_point = 0
        self.security_lowest_point = 0
        self.real_init_capital = 0
        self.real_final_capital = 0
        self.diference_percentage = 0
        self.init_date = ""
        self.end_date = ""
        self.last_decision = ""


    def last_days_results(self, days):
        """
        Function to test last n days of strategy allready trained
        """
        return self.security['Date', 'Close', 'FinalDecision'][-days:]

    def test_last_days(self, days, transactionType, transactionQuantity):
        """
        Test the las n days according to its decisions
        """
        data = self.last_days_results(days)
        


class FirstTransactionType(Enum):
    """
    Enum que define como se hara la primer practica
    """
    STOCK_QUANTITY = auto()
    INIT_CAPITAL = auto()

class TransactionType(Enum):
    """
    Enum para tipo de transaccion
    """
    BUY = auto()
    SELL = auto()
        