from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data



def get_data(security):
    param = {
        'q': security, # Stock symbol (ex: "AAPL")
        'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "BMV", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1Y" # Period (Ex: "1Y" = 1 year)
    }
    # get price data (return pandas dataframe)
    df = get_price_data(param)
    return df