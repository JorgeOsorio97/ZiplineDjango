import pandas as pd
import numpy as np

def corregir_titulos():
    hist = ['AEROMEX.csv', 'AHMSA.csv', 'AmericaMovil.csv', 'ArcaContinental-AC.csv', 'BACHOCO.csv', 'BancoSANTANDER.csv', 'BIMBO.csv', 'BMV.csv', 'Cablevision.csv', 'Casa_SABA.csv', 'CEMEX.csv', 'CHDRAUI.csv', 'Coca-Cola.csv', 'Consorcio_ARA.csv', 'ELEKTRA.csv', 'FINAMEX.csv', 'FirstMajesticSolverCorp-FMSC.csv', 'GENNOMA-LAB.csv', 'GrupoNacionalProvincial-GNP.csv', 'GrupoSports.csv', 'LIVERPOOL.csv', 'RadioCENTRO.csv', 'ROTOPLAS.csv', 'SORIANA.csv', 'TELEVISA.csv', 'WAL-MART.csv']
    #hist = ['AHMSA.csv']
    for w in hist:
        sus = [] 
        data = pd.read_csv(w)
        cols = data.columns.values
        cols = [i.title() for i in cols]
        print(type(cols[0]))
        print(cols[0])
        print(cols)
        data.columns = cols
        data.to_csv(w, index = False)


corregir_titulos()

