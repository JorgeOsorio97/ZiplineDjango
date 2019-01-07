from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

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
    return render(request, "integraRH/formularioTrabajador.html") 

def visualizadorTrabajador(request):
    return render(request, "integraRH/visualizadorTrabajador.html") 

