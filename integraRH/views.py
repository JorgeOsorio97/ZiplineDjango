from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "integraRH/index.html") 

def regristroInicialTrabajador(request):
    return render(request, "integraRH/registroInicialTrabajador.html") 

def formularioTrabajador(request):
    pass

def visualizadorTrabajador(request):
    return render(request, "integraRH/visualizadorTrabajador.html") 

