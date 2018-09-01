import pandas as pd
import datetime as dt
from ShowIndicators.get_info_wtd import get_today_data_wtd


def updateSecurity(file_name, security):
    df = pd.read_csv(file_name, index_col = 0)
    print(df.head())
    if not df['Date'].iloc[-1] == str(dt.datetime.now().year) + str(dt.datetime.now().month) + str(dt.datetime.now().day):
        today_data = get_today_data_wtd(security)
        df.append(today_data, ignore_index = True)
        print(df.head())
    df.to_csv(file_name, index = False)


