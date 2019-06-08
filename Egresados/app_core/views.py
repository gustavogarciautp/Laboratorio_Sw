from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect ##redirect sirve para redireccionar paginas
from .forms import LoginForm, Recuperar1Form, Recuperar2Form
from django.core.mail import EmailMessage
from django.urls import reverse
#from  .models import Registrarse
import hashlib
import random
from .models import Administrador, Egresado, SuperUser

# Create your views here.
def login(request, vista):
    #print("Tipo de petición: {}".format(request.method))  #method nos indica el metodo con el que se ha hecho la peticion
    login_form = LoginForm() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        login_form = LoginForm(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if login_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            email= request.POST.get('email')
            contraseña=request.POST.get('contraseña')
            contraseña_cifrada= hashlib.sha1(contraseña.encode()).hexdigest()
            try:
                if vista=='egresado':
                    obj=Egresado.objects.get(email=email, contraseña=contraseña_cifrada)
                elif vista =='administrador':
                    obj= Administrador.objects.get(email=email, contraseña=contraseña_cifrada)
                if obj:
                    if not obj.activate():
                        return redirect(reverse('login')+'?fail') #reverse('contact') es como si fuera un tag url"""
                    else:
                        return redirect(reverse('principal'))
            except:
                return redirect(reverse('login')+'?nofound')


    return render(request, "app_core/login.html", {'form':login_form})


def recuperar_1(request):
    recuperar1_form = Recuperar1Form() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        recuperar1_form = Recuperar1Form(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if recuperar1_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            email= request.POST.get('email')
            obj=Registrarse.objects.get(email=email)
            if obj:
                asunto= 'Restablece tu contraseña'
                #clave= random.randint(1000,100000)
                clave_cifrada= hashlib.sha1(str(obj.id).encode()).hexdigest()
                content= '''
                Alguien (espero que usted) haya solicitado un restablecimiento de contraseña para su cuenta del Sistema de Egresados. Siga el enlace de abajo para establecer una nueva contraseña:
                http://127.0.0.1:8000/recuperar_2/'''+str(clave_cifrada)+\
                '''
                 Si no desea restablecer su contraseña, ignore este correo electrónico y no se tomará ninguna medida.'''
                email = EmailMessage(
                    asunto,
                    content,
                    to= [email]#['gustavito_9813@hotmail.com']
                )
                email.send() #enviamos el mensaje

                obj.id_restablecimiento=clave_cifrada
                obj.save()


    return render(request, "app_core/recuperar_pass_1.html", {'form':recuperar1_form})


def recuperar_2(request, id_recuperacion):
    page= get_object_or_404(Registrarse, id_restablecimiento=id_recuperacion)
    id_recuperacion=''
    recuperar2_form = Recuperar2Form() #Hacemos la instancia del formulario
    if request.method == 'POST': #verificamos se el formulario se ha enviado por POST
        recuperar2_form = Recuperar2Form(data= request.POST) #request.POST contiene los campos que hemos rellenado en el formulario
        if recuperar2_form.is_valid():  #verifica que todos los campos esten rellenados correctamente
            contraseña= request.POST.get('contraseña')
            confirmar_contraseña = request.POST.get('confirmar_contraseña')
            if contraseña==confirmar_contraseña:
                page.id_restablecimiento=''
                page.contraseña= hashlib.sha1(contraseña.encode()).hexdigest()
                page.save()
            else:
                return redirect(reverse('recuperar_2')+'?nomatch')


    return render(request, "app_core/recuperar_pass_2.html", {'form':recuperar2_form})


def principal(request):
    return render(request, "app_core/principal.html")