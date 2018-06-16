import requests


url = 'https://marketdata.websol.barchart.com/getQuote.json'
pars = {'apikey':'e6cd91fd5766f09b6627773d8d83dfa6',
        'symbols':'AMX,CX',
        'fields': 'fiftyTwoWkHigh,fiftyTwoWkHighDate,fiftyTwoWkLow,fiftyTwoWkLowDate'}

r = requests.post(url = url,params=pars, verify = False)

print(r.status_code, r.reason)

print(r.json()['results'][0])

