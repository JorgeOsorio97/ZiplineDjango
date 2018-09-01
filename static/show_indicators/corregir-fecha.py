import pandas as pd


def corregir_fecha():
    hist = ['AEROMEX.csv', 'AMXA.csv', 'AC.csv', 'BACHOCOB.csv', 'SAN.csv', 'BIMBO.csv', 'BOLSAA.csv', 'CABLECPO.csv', 'CEMEXCPO.csv', 'CHDRAUIB.csv', 'Coca-Cola.csv', 'ARA.csv', 'ELEKTRA.csv', 'FINAMEXO.csv', 'Genomma-Lab.csv', 'GNP.csv', 'SPORTS.csv', 'RCENTROA.csv', 'AGUA.csv', 'SORIANAB.csv', 'WALMEX.csv']
    for w in hist:
        sus = [] 
        data = pd.read_csv(w)
        for x in data['FECHA']:
            y = '{0}-{2}-{1}'.format(x[6:],x[3:5],x[0:2])
            print(x)
            print(y)    
            sus.append(y)
        data['FECHA'] = sus
        data.to_csv(w, index = False)

corregir_fecha()    