from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import pandas as pd

# Create your views here.

def index(request):
    return render(request, "integraRH/index.html") 

@csrf_exempt
def regristroInicialTrabajador(request):
    context_dict={'message_sent' : False}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        print(name, email)
        #email_context = Context({'name':name}) 
        email_context = {'name':name}
        plain_message = get_template("integraRH/email.txt").render(email_context)
        html_message = get_template('integraRH/email.html').render(email_context)
        

        email = EmailMultiAlternatives("Contratación Integra",
                                        plain_message,
                                        "integra@integra.com.mx",
                                        [email])
        email.attach_alternative(html_message, "text/html")
        email.send()
        context_dict['message_sent'] = True
    return render(request, "integraRH/registroInicialTrabajador.html", context_dict) 

def formularioTrabajador(request):
    context_dict = {'trabajadorCreado' : False}
    if request.method == 'POST':
        data = pd.DataFrame([{"Nombre": request.POST['nombre'],
                        "ApellidoP":request.POST['firstln'],
                        "ApellidoM": request.POST['secondln'],
                        "EstadoCivil": request.POST['civil'],
                        "Conyuge": request.POST['couple'],
                        "Edad":request.POST['age'],
                        "RFC": request.POST['rfc'],
                        "CURP": request.POST['curp']}
                        ])
        data.to_csv("trabajador.csv", index = False)
        context_dict['trabajadorCreado'] = True
    return render(request, "integraRH/formularioTrabajador.html", context_dict) 
        

def visualizadorTrabajador(request):
    context_dict = {}
    data = pd.read_csv("trabajador.csv")
    context_dict['Nombre'] = data['Nombre'][0]
    context_dict['ApellidoP'] = data['ApellidoP'][0]
    context_dict['ApellidoM'] = data['ApellidoM'][0]
    context_dict['EstadoCivil'] = data['EstadoCivil'][0]
    context_dict['Conyuge'] = data['Conyuge'][0]
    context_dict['Edad'] = data['Edad'][0]
    context_dict['RFC'] = data['RFC'][0]
    context_dict['CURP'] = data['CURP'][0]
    data_dict = {'data': context_dict}
    return render(request, "integraRH/visualizadorTrabajador.html", data_dict) 

