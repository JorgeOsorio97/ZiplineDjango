import pandas as pd


def corregir_fecha():
    hist = ['AEROMEX.csv', 'AHMSA.csv', 'AmericaMovil.csv', 'ArcaContinental-AC.csv', 'BACHOCO.csv', 'BancoSANTANDER.csv', 'BIMBO.csv', 'BMV.csv', 'Cablevision.csv', 'Casa_SABA.csv', 'CEMEX.csv', 'CHDRAUI.csv', 'Coca-Cola.csv', 'Consorcio_ARA.csv', 'ELEKTRA.csv', 'FINAMEX.csv', 'FirstMajesticSolverCorp-FMSC.csv', 'GENNOMA-LAB.csv', 'GrupoNacionalProvincial-GNP.csv', 'GrupoSports.csv', 'LIVERPOOL.csv', 'RadioCENTRO.csv', 'ROTOPLAS.csv', 'SORIANA.csv', 'TELEVISA.csv', 'WAL-MART.csv']
    for w in hist:
        sus = [] 
        data = pd.read_csv(w)
        for x in data['FECHA']:
            y = '{}-{}-{}'.format(x[6:],x[3:5],x[0:2])
            print(x)
            print(y)
            sus.append(y)
        data['FECHA'] = sus
        data.to_csv(w, index = False)

corregir_fecha()