from requests import request
import numpy as np
import pandas as pd
import csv

def get_data_wtd(security):
    api_username = 'b4JhSRB8Nyr2rh8cpY7EHadcABGkhBejjwQK7hAM0xWd1LRPDUnbcXr647Pi'
    base_url = "https://www.worldtradingdata.com/api/v1/"

    bmv = '.MX'

    request_url = base_url + "history/"
    q_params = {
        'symbol': security + bmv,
        'api_token': api_username,
        'date_from': '2007-01-01',
        'date_to': '2018-06-04',
        'output':'csv'       
    }

    response = request('GET',request_url, params = q_params)
    x = (str(response.content)[2:-3].split('\\n'))
    t = list(z.split(',') for z in x)
    df = pd.DataFrame(data = t[1:],columns=t[0])
    return df


print(get_data_wtd('AGUA'))
    