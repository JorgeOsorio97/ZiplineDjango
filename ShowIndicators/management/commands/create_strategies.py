from django.core.management.base import BaseCommand, CommandError
from ShowIndicators.models import Securities
import pandas as pd
import datetime as dt
from ShowIndicators.get_info_wtd import get_today_data_wtd
from ShowIndicators.simulator.strategies_utils import createStrategy


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('quantity', nargs='+', type=int)
        # Named (optional) arguments
        parser.add_argument(
            '--quantity',
            action='store_true',
            dest='quantity',
            help='Define how many strategies create per security',
        )

    

    def handle(self, *args, **options):
        secs = Securities.objects.values('id', 'security', 'market', 'csv_file','last_update')
        secs = list(secs)
        quantity = 10
        if(options['quantity']):
            quantity = options['quantity'][0]
        for sec in secs:
            secObject = Securities.objects.get(id = sec['id'])
            createStrategy(pd.read_csv('static/historicos/'+ sec['csv_file']), secObject, tries = quantity)
        
    