from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from . import simulator, indicators, strategies_utils, forms
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json, csv
from ShowIndicators.models import Securities
from datetime import datetime

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
    strategy_temp = strategy.iloc[0]["Strategy"]
    for key, value in securities_dict.items():    # for name, age in list.items():  (for Python 3.x)
        if value == security:
            symbol = key
    symbol = pd.read_csv('static/historicos/'+securities_dict[symbol]+'.csv')
    print(strategy)
    sim = strategies_utils.jsonStrategyToSim(strategy_temp, symbol)
    return JsonResponse({'strategy': json.loads(strategy_temp), '%Up': strategy['%Up'].iloc[0], 'decision':sim.last_decision})


def addSecurity(request):
    if request.method == "POST":
        print("add_security_file")
        print(request.FILES)
        data = pd.read_csv(request.FILES['file'])
        #print(data.head())
        #TODO agregar try para evita cargar errores
        #TODO agregar revision de securities repetidos
        #TODO agregar descarga de plantilla
        for index, row in data.iterrows():
            temp = Securities()
            temp.security = row['security']
            temp.name = row['name']
            temp.market = row['market']
            temp.stock_own = row['stocks_own']
            temp.providers_name = json.dumps({row['provider']:row['ticker']})
            temp.csv_file = row['csv_file']
            temp.save()

    form = forms.UploadFileForm()
    #print(form)
    return render(request, 'show_indicators/add_security.html', {'form': form})

@csrf_exempt
def newSecurity(request):
    print("new_security")
    print(request.POST)
    return JsonResponse({"succes":True})
