from django.core.management.base import BaseCommand, CommandError
from ShowIndicators.models import Securities
import pandas as pd
import datetime as dt
from ShowIndicators.get_info_wtd import get_today_data_wtd
from ShowIndicators.simulator.strategies_utils import updateSecurity


class Command(BaseCommand):
    secs = Securities.objects.values('id', 'security', 'market', 'csv_file','last_update')
    secs = list(secs)

    def handle(self, *args, **options):
        for sec in self.secs:
            updateSecurity(sec['csv_file'],sec['security'])
            temp = Securities.objects.get(id=sec['id'])
            temp.last_update = dt.date.today()
            temp.save()
    