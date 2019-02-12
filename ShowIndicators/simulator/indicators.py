import pandas as pd
import numpy as np
from talib import EMA, KAMA, SAR, SMA, TEMA, TRIMA, WMA # pylint: disable=E0611

def EMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = EMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}

def KAMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = KAMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}

def SARdecision(table, aceleration = 0.02, max = 0.2):   
    decision = []
    high =table['High']
    low = table['Low']

    del table
    data = SAR(np.array(high), np.array(low), aceleration, max)
    

    for i in np.arange(len(high)):     
        if np.isnan(data[i]):
            decision.append(None)
        elif data[i] >= low[i]:
            decision.append('Buy') 
        elif data[i] <= high[i]:
            decision.append('Sell')
        else:
            decision.append(decision[-1])  

    
    return {'decision' :decision, 'data': data}

def SMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = SMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}

def TEMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = TEMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}

def TRIMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = TRIMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}

def WMAdecision(table, days = 20):   
    decision = []
    close =table['Close']
    del table
    data = WMA(np.array(close),days)

    for i in np.arange(len(close)):     
        if np.isnan(data[i]):
            decision.append(None)
        if data[i] > close[i]:
            decision.append('Sell') 
        if data[i] < close[i]:
            decision.append('Buy')  
    return {'decision' :decision, 'data': data}


#TODO revisar el csv de aeromex con los del koala en dropbox