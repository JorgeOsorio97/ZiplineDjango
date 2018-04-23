from requests import request
import numpy as np
import pandas

def intrinio_security():
    api_username = '8993a7d350ddc80795097189caecf28b'
    api_password = '7f74a16a497c5f27204b15eebd3eeeae'
    base_url = "https://api.intrinio.com"

    bmv = '^XMEX'

    request_url = base_url + '/historical_data'
    q_params = {
        'identifier' '',
        'item': 'close_price',
        'start_date': '2007-01-01',
        'end_date': '2018-06-04',   
        'frequency': 'daily',
    }

    response = request('GET',request_url, params = q_params, auth=(api_username, api_password))

    data = response.json()['data']
    n_pages = response.json()['total_pages']
    print(n_pages)

    cols = ['Date','Open', 'High', 'Low', 'Close', 'Volume']

    df = pd.DataFrame(cols = cols,)

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