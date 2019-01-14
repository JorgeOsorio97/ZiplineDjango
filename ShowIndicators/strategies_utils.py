from ShowIndicators.indicators import EMAdecision, SARdecision, KAMAdecision, SMAdecision, TEMAdecision, TRIMAdecision, WMAdecision # pylint: disable=E0401
from ShowIndicators.simulator import Simulator
from ShowIndicators.models import Securities, Strategies, Result
from ShowIndicators.get_info_wtd import get_all_data_wtd
import pandas as pd
import numpy as np
import datetime as dt
import json
import os


from ZiplineDjango.settings.base import STATIC_DIR


def testStrategy(data, security, tries = 100):
    result = []

    for i in range(tries): # pylint: disable=W0612
        strategy = {}
        sim = Simulator(data, std_purchase= 10)

        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('EMA-{}'.format(days),EMAdecision(data,days))
            strategy.update({'EMA':{'parameters':{'days':days}}})
            #TODO crear funcion para agregar parametros automatico
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('KAMA-{}'.format(days),KAMAdecision(data,days))
            strategy.update({'KAMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('SMA-{}'.format(days),SMAdecision(data,days))
            strategy.update({'SMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('TEMA-{}'.format(days),TEMAdecision(data,days))
            strategy.update({'TEMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('TRIMA-{}'.format(days),TRIMAdecision(data,days))
            strategy.update({'TRIMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('WMA-{}'.format(days),WMAdecision(data,days))
            strategy.update({'WMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            acel = np.random.randint(20,100)/1000
            maxacel = np.random.randint(20,100)/100
            sim.add_indicator('SAR-{}-{}'.format(acel, maxacel), SARdecision(data,aceleration = acel, max = maxacel))
            strategy.update({'SAR':{'parameters':{'aceleration':acel, 'max_aceleration':maxacel}}})
        sim.calc_earning()
        strategy = json.dumps(strategy)
        iteration_result =[security,strategy, sim.real_final_capital, sim.diference_percentage]
        print(iteration_result)
        result.append(iteration_result)
        sqlappend = Strategies(security = security, strategy = strategy, percentage_up= sim.diference_percentage, trades = sim.operations_made, max_point = sim.highest_point, min_point = sim.lowest_point )
        print(sqlappend)
        sqlappend.save()
        sim.cleanSimulator()

    cols = ['Security','Strategy','Final_Capital','%Up']
    result = pd.DataFrame(result, columns=cols)
    
def findBestStrategy(security):
    all_strategies = []
    for i in list(Strategies.objects.all().values().filter(security=security)): #pylint: disable = E1101
        all_strategies.append([i['id'], i['security'], i['strategy'], i['percentage_up'], i['last_modified'], i['max_point'],i['min_point'], i['trades']])
    #print(all_strategies[0])
    all_strategies = pd.DataFrame(all_strategies, columns = ['id','Security','Strategy','%Up','LastModified','MaxPoint', 'MinPoint', 'Trades'])
    #security_strategies = all_strategies[all_strategies['Security']==security]
    security_strategies = all_strategies

    best_strategy = security_strategies[ security_strategies['%Up'] == security_strategies['%Up'].max()]
    print(best_strategy)
    return best_strategy

def jsonStrategyToSim(strategy, data):
    strategy = json.loads(strategy)
    sim = Simulator(data, std_purchase = 10)
    for indicator , val in strategy.items():
        indicator_name = '{}'.format(indicator)
        for param , value in val['parameters'].items():
            indicator_name += '-{}'.format(value)
        sim.add_indicator(indicator_name, defineStrategyFunction(indicator_name, data))
        sim.calcDecision()
    return sim

def defineStrategyFunction(indicator_name, data):
    indicator_name = indicator_name.split('-')
    for i in range(len(indicator_name)):
        if i == 0:
            pass
        else:
            indicator_name[i] = float(indicator_name[i])
    if indicator_name[0] == 'EMA':
        return EMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'KAMA':
        return KAMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'SMA':
        return SMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'TEMA':
        return TEMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'TRIMA':
        return TRIMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'WMA':
        return WMAdecision(data,indicator_name[1])
    elif indicator_name[0] == 'SAR':
        return SARdecision(data,indicator_name[1], indicator_name[2])
    else:
        print('ERROR GRAVE NO SE ENCONTRO EL INDICADOR')
    return

def updateSecurity(file_name, security):
    file_name = os.path.join(os.path.join(STATIC_DIR,"historicos"),file_name)
    print(file_name)
    #df = pd.read_csv(file_name)
    #print(df.tail())
    # TODO: hacer que solo atualice un dia
    #if not df['Date'].iloc[-1] == str(dt.datetime.now().year) + str(dt.datetime.now().month) + str(dt.datetime.now().day):
    today_data = get_all_data_wtd(security)
    #df.append(today_data, ignore_index = True)
    #print(df.head())
    today_data.to_csv(file_name, index = False)
    
    #df.to_csv(file_name, index = False)


def createStrategy(data, security, tries = 20):
    result = []

    for i in range(tries): # pylint: disable=W0612
        strategy = {}
        sim = Simulator(data, std_purchase= 10)

        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('EMA-{}'.format(days),EMAdecision(data,days))
            strategy.update({'EMA':{'parameters':{'days':days}}})
            #TODO crear funcion para agregar parametros automatico
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('KAMA-{}'.format(days),KAMAdecision(data,days))
            strategy.update({'KAMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('SMA-{}'.format(days),SMAdecision(data,days))
            strategy.update({'SMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('TEMA-{}'.format(days),TEMAdecision(data,days))
            strategy.update({'TEMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('TRIMA-{}'.format(days),TRIMAdecision(data,days))
            strategy.update({'TRIMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            days = np.random.randint(20,100)
            sim.add_indicator('WMA-{}'.format(days),WMAdecision(data,days))
            strategy.update({'WMA':{'parameters':{'days':days}}})
        if np.random.randint(0,2)==1:
            acel = np.random.randint(20,100)/1000
            maxacel = np.random.randint(20,100)/100
            sim.add_indicator('SAR-{}-{}'.format(acel, maxacel), SARdecision(data,aceleration = acel, max = maxacel))
            strategy.update({'SAR':{'parameters':{'aceleration':acel, 'max_aceleration':maxacel}}})
        sim.calc_earning()
        strategy = json.dumps(strategy)
        iteration_result =[security,strategy, sim.real_final_capital, sim.diference_percentage]
        print(iteration_result)
        result.append(iteration_result)
        strategy_append = Strategies(security = security, strategy = strategy, percentage_up= sim.diference_percentage, trades = sim.sells_made + sim.buys_made, max_point = sim.highest_point, min_point = sim.lowest_point )
        strategy_append.save()
        result_append = Result(strategy = strategy_append, security = security, percentage_up = sim.diference_percentage, buy_trades = sim.buys_made, sell_trades = sim.sells_made, max_point = sim.highest_point, min_point = sim.lowest_point)
        result_append.save()
        sim.cleanSimulator()
    
def setBestStrategy():
    secs = Securities.objects.all()
    for sec in secs:
        best = findBestStrategy(sec.security)
        best = Strategies.objects.get(id =  best['id'])
        sec.best_strategy = best
        sec.save()