import pandas as pd
import os

def prom_mov_short(dir, dias = 20):
    symbol = pd.read_csv(dir)
    #print(symbol.head(5))
    list=[]
    suma_i = 0
    t=0
    suma_f = 0
    for x in range(dias-1):
        list.append(0)
    for i in range(len(symbol['CIERRE'])-dias+1):
        suma_i = 0
        for j in range(dias):
            suma_i += symbol['CIERRE'][i+j]
        t +=1
        prom1 = suma_i/dias
        suma_f += prom1
        list.append(prom1)
    symbol['ProMovShort']= list
    #print(symbol.head(21))
    symbol.to_csv('ShowIndicators/result.csv')

def prom_mov_long(dir, dias = 50):
    symbol = pd.read_csv(dir)
    #print(symbol.head(5))
    list=[]
    suma_i = 0
    t=0
    suma_f = 0
    for x in range(dias-1):
        list.append(0)
    for i in range(len(symbol['CIERRE'])-dias+1):
        suma_i = 0
        for j in range(dias):
            suma_i += symbol['CIERRE'][i+j]
        t +=1
        prom1 = suma_i/dias
        suma_f += prom1
        list.append(prom1)
    symbol['ProMovLong']= list
    #print(symbol.head(21))
    symbol.to_csv('ShowIndicators/result.csv')