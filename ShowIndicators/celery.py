from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZiplineDjango.settings.base')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()

app.conf.update(
    BROKER_URL = 'sqs://AKIAIXPPXFTW77RSDS7A:FGXzxmBI3dMiE3Em1cTWgnBJyhXol49VgFGV8TOF@'
)