from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from ShowIndicators import simulator, indicators, strategies_utils, update_security
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json

#TODO general de views corregir los csrf exempt agregando a cookies el csrf

securities_dict = {'aeromex' : 'AEROMEX',
                    'americaMovil' : 'AMXA', 
                    'arcaContinental' : 'AC',
                    'bachoco' : 'BACHOCOB',
                    #'bancoSantander' : 'SAN',  ## eliminado por falta de datos
                    'bimbo' : 'BIMBO',
                    'bmv' : 'BOLSAA', 
                    'cablevision' : 'CABLECPO', 
                    'cemex' : 'CEMEXCPO',
                    'chedrahui' : 'CHDRAUIB', 
                    'cocacola' : 'Coca-Cola', 
                    'consorcioAra' : 'ARA', 
                    'elektra' : 'ELEKTRA', 
                    'finamex': 'FINAMEXO', 
                    'gennomaLab' : 'Genomma-Lab', 
                    'gnp' : 'GNP', 
                    'grupoSports' : 'SPORTS', 
                    'radioCentro' : 'RCENTROA', 
                    'rotoplas' : 'AGUA', 
                    'soriana' : 'SORIANAB', 
                    'walmart' : 'WALMEX'
                    }

# Create your views here.
def index(request):
    print('index')
    #getData(request)
    return render(request, 'show_indicators/index.html')

@csrf_exempt
def getData(request):
    req_url = request.POST['security'] 
    indicators_req = dict(request.POST.lists())['indicators[]']
    symbol = pd.read_csv('static/show_indicators/historicos/'+securities_dict[req_url]+'.csv')
    sim  = simulator.Simulator(symbol,std_purchase = 20)
    #TODO hacer que se agreguen dinamicamente los indicadores
    sim.add_indicator('SMA-50',indicators.SMAdecision(symbol,50))
    sim.add_indicator('SMA-20',indicators.SMAdecision(symbol,20))
    sim.security.to_csv('ShowIndicators/result.csv', index = False)
    fileUrl = 'result.csv'
    return JsonResponse({'URL' : fileUrl, 'indicators':[]})   

def result(request):
    with open('ShowIndicators/result.csv', 'rb') as myfile:
        response = HttpResponse(myfile, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=result.csv'
        return response

@csrf_exempt
def pruebasPost(request):
    return JsonResponse({'succes': True})


@csrf_exempt
def callBestStrategy(request):
    print('callBestStrategy View')
    security = request.POST['security']
    security = securities_dict[security]
    # for x in securities_dict: #for para crear estrategias
    #        strategies_utils.testStrategy(pd.read_csv('static/show_indicators/historicos/'+securities_dict[x]+'.csv'),securities_dict[x], tries = 1)
    strategy = strategies_utils.findBestStrategy(security)
    if len(strategy)>1:
        strategy_temp = strategy['Strategy'].iloc[0]
    else:
        strategy_temp=strategy['Strategy']
    for key, value in securities_dict.items():    # for name, age in list.items():  (for Python 3.x)
        if value == security:
            symbol = key
    symbol = pd.read_csv('static/show_indicators/historicos/'+securities_dict[symbol]+'.csv')
    print(strategy)
    sim = strategies_utils.jsonStrategyToSim(strategy_temp, symbol)
    return JsonResponse({'strategy': json.loads(strategy_temp), '%Up': strategy['%Up'].iloc[0], 'decision':sim.last_decision})


def add_security(request):
    return render(request, 'show_indicators/add_security.html')