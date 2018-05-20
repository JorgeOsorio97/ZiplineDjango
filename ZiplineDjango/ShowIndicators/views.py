from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    print('index')
    #getData(request)
    
    return render(request, 'show_indicators/index.html')

def getData(request):
    print("si entro")
    securities_dict = {'aeromex' : 'AEROMEX.csv', 'ahmsa' : 'AHMSA.csv',
                    'americaMovil' : 'AmericaMovil.csv', 'arcaContinental' : 'ArcaContinental-AC.csv',
                    'bachoco' : 'BACHOCO.csv', 'bancoSantander' : 'BancoSANTANDER.csv', 
                    'bimbo' : 'BIMBO.csv', 'bmv' : 'BMV.csv', 'cablevision' : 'Cablevision.csv', 
                    'casaSaba' : 'Casa_SABA.csv', 'cemex' : 'CEMEX.csv', 'chedrahui' : 'CHDRAUI.csv', 
                    'cocacola' : 'Coca-Cola.csv', 'consorcioAra' : 'Consorcio_ARA.csv', 
                    'elektra' : 'ELEKTRA.csv', 'finamex': 'FINAMEX.csv', 
                    'firstMajesticSolveCorpFmsc' : 'FirstMajesticSolverCorp-FMSC.csv', 
                    'gennomaLab' : 'GENNOMA-LAB.csv', 'gnp' : 'GrupoNacionalProvincial-GNP.csv', 
                    'grupoSports' : 'GrupoSports.csv', 'liverpool' : 'LIVERPOOL.csv', 
                    'radioCentro' : 'RadioCENTRO.csv', 'rotoplas' : 'ROTOPLAS.csv', 
                    'soriana' : 'SORIANA.csv', 'televisa' : 'TELEVISA.csv', 'walmart' : 'WAL-MART.csv'} 
    req_url = request.GET.get('url')
    print(req_url)
    fileUrl = 'static/show_indicators/historicos/result.csv'
    return JsonResponse({'URL' : fileUrl}) 