from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from ShowIndicators import indicators,simulator
import csv
import io
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    print('index')
    #getData(request)
    
    return render(request, 'show_indicators/index.html')

@csrf_exempt
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
    print(request.POST)
    req_url = request.POST['security'] 
    indicators_req = dict(request.POST.lists())['indicators[]']
    print(req_url)
    print(securities_dict[req_url])
    print(indicators_req)
    symbol = pd.read_csv('static/show_indicators/historicos/'+securities_dict[req_url])
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

