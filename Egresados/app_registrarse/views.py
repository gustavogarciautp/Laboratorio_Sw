# Create your views here.

from django.shortcuts import render, redirect ##redirect sirve para redireccionar paginas
from .forms import RegistroForm
from .models import Perfil
from django.core.mail import EmailMessage
from django.urls import reverse
from  app_core.models import Egresado, Interes
from datetime import datetime
import hashlib
import requests
import urllib
import json
from django import forms
from django.conf import settings
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django .urls import reverse_lazy
from django.forms.widgets import CheckboxSelectMultiple

def update():
    obj= Interes.objects.all()
    INTERESES=[]
    for interes in obj:
        INTERESES.append([interes.nombre,interes.nombre])
    return INTERESES

def registrarse(request):
    registro_form = RegistroForm() #Hacemos la instancia del formulario
    INTERESES=update()
    registro_form.fields['interes_']= forms.MultipleChoiceField(
							            required=True,
							            label='Interes',
							            widget=CheckboxSelectMultiple(),
							            choices=INTERESES)
    #print(registro_form.nombres)
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

            myDict = request.POST.dict()
            print(type(myDict))
            #print(myDict)
            words=(request.POST.getlist('interes_'))
            print(words)
            print(request.POST.get('interes_'[0]))
            print(request.POST.get('interes_'[1]))


            obj = Egresado.objects.create(nombres=nombres, apellidos=apellidos, pais=pais, fecha_nacimiento=date, genero=genero,email=email, contraseña= contraseña_cifrada, activacion= activacion)

            return redirect(reverse('login'))


    return render(request, "app_registrarse/registrarse.html", {'form': registro_form})



class ProfileUpdate(UpdateView):
	model = Perfil
	fields = ['avatar', 'bio', 'link']
	success_url = reverse_lazy('perfil')
	template_name= 'app_registarse/perfil_form.html'

	def get_object(self):
		#recuperar el objeto que se va a editar
		perfil, creado= Perfil.objects.get_or_create(user=self.request.user)
		return perfil