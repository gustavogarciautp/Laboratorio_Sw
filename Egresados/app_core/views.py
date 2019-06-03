from django.shortcuts import render

from django.shortcuts import render, redirect ##redirect sirve para redireccionar paginas
from .forms import LoginForm
from django.core.mail import EmailMessage
from django.urls import reverse
#from  .models import Registrarse
import hashlib

# Create your views here.
def login(request):
    #print("Tipo de petición: {}".format(request.method))  #method nos indica el metodo con el que se ha hecho la peticion
    login_form = LoginForm() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        login_form = LoginForm(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if login_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            email= request.POST.get('email')
            contraseña=request.POST.get('contraseña')
            contraseña_cifrada= hashlib.sha1(contraseña.encode()).hexdigest()

            obj = Registrarse.objects.create(nombres=nombres, apellidos=apellidos, pais=pais, fecha_nacimiento=date, genero=genero,email=email, contraseña= contraseña_cifrada, activacion= activacion)
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
    return render(request, "app_core/login.html", {'form':login_form})
