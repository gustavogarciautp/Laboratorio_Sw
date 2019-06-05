# Create your views here.

from django.shortcuts import render, redirect ##redirect sirve para redireccionar paginas
from .forms import RegistroForm
from django.core.mail import EmailMessage
from django.urls import reverse
from  .models import Registrarse
from datetime import datetime
import hashlib
import requests
import urllib
import json
from django.conf import settings
from django.contrib import messages


# Create your views here.
def registrarse(request):
    #print("Tipo de petición: {}".format(request.method))  #method nos indica el metodo con el que se ha hecho la peticion
    registro_form = RegistroForm() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        registro_form = RegistroForm(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if registro_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            nombres= request.POST.get('nombres')  #request es un diccionario por eso utilizamos get para obtener los valores

            apellidos = request.POST.get('apellidos')
            pais = request.POST.get('pais')

            fecha_nacimiento_month= request.POST.get('fecha_nacimiento_month')
            fecha_nacimiento_day= request.POST.get('fecha_nacimiento_day')
            fecha_nacimiento_year= request.POST.get('fecha_nacimiento_year')
            date=datetime(int(fecha_nacimiento_year),
            				int(fecha_nacimiento_month),
            				int(fecha_nacimiento_day))

            print(request.POST)
            print(request.POST.get('fecha_nacimiento_month'))

            email= request.POST.get('email')
            genero=request.POST.get('genero')
            contraseña=request.POST.get('contraseña')
            contraseña_cifrada= hashlib.sha1(contraseña.encode()).hexdigest()
            activacion=False
            #content= request.POST.get('content','')
            #Enviamos el correo y redireccionamos
            """email = EmailMessage(
               'La caffetiera: Nuevo mensaje de contacto', #este es el asunto
               'De {} <{}>\n\nEscribio:\n\n{}'.format(name,email, content), #este es el cuerpo del mensaje
                'no-contestar@inbox.mailtrap.io', #email de origen
                ['gustavito_98153@hotmail.com'],#email_destino
                reply_to=[email] #este es el email donde va a responder la persona que recibe el correo
            )
            try:
                email.send() #enviamos el mensaje
                #Todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo no ha ido bien, redireccionamos a fail
                return redirect(reverse('contact')+'?fail') #reverse('contact') es como si fuera un tag url"""
    
            recaptcha_response = request.POST.get('captcha')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            verificar = requests.get(url, values)
            verificar = verificar.json()
            print(verificar)
            response = verificar.get("success",False)

            """
            print("SUCCESS 1")
            req =  urllib.request.Request(url, data=data)
            print(req)
            response = urllib.request.urlopen(req)
            print("SUCCESS 3")
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            print(result)"""
            if result['success']:
                form.save()
                obj = Registrarse.objects.create(nombres=nombres, apellidos=apellidos, pais=pais, fecha_nacimiento=date, genero=genero,email=email, contraseña= contraseña_cifrada, activacion= activacion)
                print("SUCCESS")
                messages.success(request, 'Registrado con exito')
            else:
                messages.error(request, 'CAPTCHA invalido. Por favor intentalo de nuevo.')

            return redirect('registrarse')

    return render(request, "app_registrarse/registrarse.html", {'form':registro_form})
