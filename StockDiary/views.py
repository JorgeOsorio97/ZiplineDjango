from django.shortcuts import render
from StockDiary.models import Transaction

# Create your views here.


def index(request):
    
    return

def buyStock(request):
    security = request.POST['security']

    return