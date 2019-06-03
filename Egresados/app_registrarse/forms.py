from django import forms
from django.utils.timezone import now

PAISES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)

GENEROS= (
	('Masculino','Masculino'),
	('Femenino', 'Femenino'),
	('Otros', 'Otros'),
	)

years=[i for i in range(1930,2019)]
#months= ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre", "Noviembre", "Diciembre"]
MONTHS = {
    1: ('Enero'), 2: ('Febrero'), 3: ('Marzo'), 4: ('Abril'), 5: ('Mayo'), 6: ('Junio'),
    7: ('Julio'), 8: ('Agosto'), 9: ('Septiembre'), 10: ('Octubre'), 11: ('Noviembre'),
    12: ('Dieciembre')
}
class RegistroForm(forms.Form):
    nombres = forms.CharField(label="Nombres", required=True, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tus nombres'}
    ), max_length=100)

    apellidos = forms.CharField(label="Apellidos", required=True, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tus apellidos'}
    ), max_length=100)

    pais = forms.CharField(label="Pais", required=True, widget= forms.Select(choices=PAISES)) 
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento",required =False, widget=forms.SelectDateWidget()) #campo opcional 
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tu email'}), max_length=100, min_length=3) #campo opcional
    
    genero= forms.CharField(label="Genero", required=False, widget= forms.Select(choices=GENEROS)) 
    contraseña = forms.CharField(label="Contraseña", required=True, widget= forms.PasswordInput()) 
