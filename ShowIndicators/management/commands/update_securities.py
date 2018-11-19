from django.core.management.base import BaseCommand, CommandError
from ShowIndicators.models import Securities
import pandas as pd
import datetime as dt
from ShowIndicators.get_info_wtd import get_today_data_wtd


class Command(BaseCommand):
    secs = Securities.objects.values('id', 'security', 'market', 'csv_file','last_update')
    secs = list(secs)
    def add_arguments(self, parser):
        #super.add_arguments(self, parser)
        pass

    def handle(self, *args, **options):
        for sec in self.secs:
            updateSecurity(sec['csv_file'],sec['security'])
            temp = Securities.objects.get(id=sec['id'])
            temp.last_update = str(dt.datetime.now().year) + str(dt.datetime.now().month) + str(dt.datetime.now().day)
            temp.save()
    




def updateSecurity(file_name, security):
    df = pd.read_csv(file_name, index_col = 0)
    print(df.head())
    if not df['Date'].iloc[-1] == str(dt.datetime.now().year) + str(dt.datetime.now().month) + str(dt.datetime.now().day):
        today_data = get_today_data_wtd(security)
        df.append(today_data, ignore_index = True)
        print(df.head())
    df.to_csv(file_name, index = False)
