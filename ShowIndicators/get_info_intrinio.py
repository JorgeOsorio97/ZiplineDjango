from requests import request
import numpy as np
import pandas as pd

def intrinio_security():
    api_username = 'c6ac93b0501d1b82172c19fdca93dfc4'
    api_password = '42af81ccd05ebf983d1c2ac2f197f2d0'
    base_url = "https://api.intrinio.com"

    bmv = 'XMEX'

    request_url = base_url + '/historical_data'
    q_params = {
        'identifier': '1',
        'item': 'close_price',
        'start_date': '2007-01-01',
        'end_date': '2018-06-04',       
        'frequency': 'daily',
    }

    response = request('GET',request_url, params = q_params, auth=(api_username, api_password))

    data = response.json()['data']
    n_pages = response.json()['total_pages']
    print(n_pages)

    col = ['Date','Open', 'High', 'Low', 'Close', 'Volume']

    df = pd.DataFrame(columns = col)

    for x in np.arange(n_pages):

        for row in data:
            date = row['date']
            value = row['value']
            print(date + ' - ' + value)
            
    return df

def call_csv():
    df = pd.read_csv('appl.csv')
    df = df.to_dict()   
    return df 