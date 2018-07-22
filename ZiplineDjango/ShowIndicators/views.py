from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from ShowIndicators import simulator, indicators, strategyLooper
import csv
import io
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json

securities_dict = {'aeromex' : 'AEROMEX', 'ahmsa' : 'AHMSA',
                    'americaMovil' : 'AmericaMovil', 'arcaContinental' : 'ArcaContinental-AC',
                    'bachoco' : 'BACHOCO', 'bancoSantander' : 'BancoSANTANDER', 
                    'bimbo' : 'BIMBO', 'bmv' : 'BMV', 'cablevision' : 'Cablevision', 
                    'casaSaba' : 'Casa_SABA', 'cemex' : 'CEMEX', 'chedrahui' : 'CHDRAUI', 
                    'cocacola' : 'Coca-Cola', 'consorcioAra' : 'Consorcio_ARA', 
                    'elektra' : 'ELEKTRA', 'finamex': 'FINAMEX', 
                    'firstMajesticSolveCorpFmsc' : 'FirstMajesticSolverCorp-FMSC', 
                    'gennomaLab' : 'GENNOMA-LAB', 'gnp' : 'GrupoNacionalProvincial-GNP', 
                    'grupoSports' : 'GrupoSports', 'liverpool' : 'LIVERPOOL', 
                    'radioCentro' : 'RadioCENTRO', 'rotoplas' : 'ROTOPLAS', 
                    'soriana' : 'SORIANA', 'televisa' : 'TELEVISA', 'walmart' : 'WAL-MART'} 

# Create your views here.
def index(request):
    print('index')
    #getData(request)
    return render(request, 'show_indicators/index.html')

@csrf_exempt
def getData(request):
    print("si entro")
    
    print(request.POST)
    req_url = request.POST['security'] 
    indicators_req = dict(request.POST.lists())['indicators[]']
    print(req_url)
    print(securities_dict[req_url])
    print(indicators_req)
    symbol = pd.read_csv('static/show_indicators/historicos/'+securities_dict[req_url]+'.csv')
    sim  = simulator.Simulator(symbol,std_purchase = 20)
    sim.add_indicator('SMA-50',indicators.SMAdecision(symbol,50))
    sim.add_indicator('SMA-20',indicators.SMAdecision(symbol,20))
    sim.security.to_csv('ShowIndicators/result.csv')
    fileUrl = 'result.csv'
    print(sim.security.tail())
    return JsonResponse({'URL' : fileUrl,
                        'indicators':[]})   

def result(request):
    with open('ShowIndicators/result.csv', 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=result.csv'
        return response

@csrf_exempt
def pruebasPost(request):
    print(request.POST)
    return JsonResponse({'succes': True})


@csrf_exempt
def callBestStrategy(request):
    print('callBestStrategy View')
    security = request.POST['security']
    security = securities_dict[security]
    strategyLooper.testStrategy(pd.read_csv('static/show_indicators/historicos/'+security+'.csv'),security, tries = 1)
    strategy = strategyLooper.findBestStrategy(security)
    print(strategy)
    return JsonResponse({'strategy': json.loads(strategy['Strategy'].iloc[0]), '%Up': strategy['%Up'].iloc[0]}) 
