from requests import request
import numpy as np
import pandas as pd
import csv
import datetime as dt


api_username = 'b4JhSRB8Nyr2rh8cpY7EHadcABGkhBejjwQK7hAM0xWd1LRPDUnbcXr647Pi'
base_url = "https://www.worldtradingdata.com/api/v1/history/"
bmv = '.MX'
today = str(dt.datetime.now().year) + '-' + str(dt.datetime.now().month) + '-' + str(dt.datetime.now().day)

def get_all_data_wtd(security):
    q_params = {
        'symbol': security + bmv,
        'api_token': api_username,
        #'date_from': '2007-01-01',
        'date_to': today,
        'output':'csv'       
    }

    response = request('GET',base_url, params = q_params)
    #print(response.content)
    x = (str(response.content)[2:-3].split('\\n'))
    t = list(z.split(',') for z in x)
    df = pd.DataFrame(data = list(reversed(t[1:])),columns=t[0])
    return df

def get_today_data_wtd(security):
    q_params = {
        'symbol': security + bmv,
        'api_token': api_username,
        'date_from': today,
        'date_to': today,
        'output':'csv'       
    }

    response = request('GET',base_url, params = q_params)
    x = (str(response.content)[2:-3].split('\\n'))
    t = list(z.split(',') for z in x)
    df = pd.DataFrame(data = reversed(t[1:]),columns=t[0])
    return df.iloc[0]


data = get_all_data_wtd('AC')
print(data.head())
print(data.tail())
