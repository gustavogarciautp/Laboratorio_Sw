from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from app_core.models import Interes
from django.forms.widgets import CheckboxSelectMultiple
from django.views.generic.base import TemplateView
from .models import Perfil

from app_core.models import Paises, Ciudades, Egresado

COUNTRIES=["Afganistán", "Akrotiri", "Albania", "Alemania", "Andorra", "Angola", "Anguila", "Antártida", "Antigua y Barbuda", "Antillas Neerlandesas", "Arabia Saudí", "Arctic Ocean", "Argelia", "Argentina", "Armenia", "Aruba", "Ashmore andCartier Islands", "Atlantic Ocean", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bahráin", "Bangladesh", "Barbados", "Bélgica", "Belice", "Benín", "Bermudas", "Bielorrusia", "Birmania Myanmar", "Bolivia", "Bosnia y Hercegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi", "Bután", "Cabo Verde", "Camboya", "Camerún", "Canadá", "Chad", "Chile", "China", "Chipre", "Clipperton Island", "Colombia", "Comoras", "Congo", "Coral Sea Islands", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dhekelia", "Dinamarca", "Dominica", "Ecuador", "Egipto", "El Salvador", "El Vaticano", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Etiopía", "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Gaza Strip", "Georgia", "Ghana", "Gibraltar", "Granada", "Grecia", "Groenlandia", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea Ecuatorial", "Guinea-Bissau", "Guyana", "Haití", "Honduras", "Hong Kong", "Hungría", "India", "Indian Ocean", "Indonesia", "Irán", "Iraq", "Irlanda", "Isla Bouvet", "Isla Christmas", "Isla Norfolk", "Islandia", "Islas Caimán", "Islas Cocos", "Islas Cook", "Islas Feroe", "Islas Georgia del Sur y Sandwich del Sur", "Islas Heard y McDonald", "Islas Malvinas", "Islas Marianas del Norte", "IslasMarshall", "Islas Pitcairn", "Islas Salomón", "Islas Turcas y Caicos", "Islas Vírgenes Americanas", "Islas Vírgenes Británicas", "Israel", "Italia", "Jamaica", "Jan Mayen", "Japón", "Jersey", "Jordania", "Kazajistán", "Kenia", "Kirguizistán", "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macao", "Macedonia", "Madagascar", "Malasia", "Malaui", "Maldivas", "Malí", "Malta", "Man, Isle of", "Marruecos", "Mauricio", "Mauritania", "Mayotte", "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montserrat", "Mozambique", "Namibia", "Nauru", "Navassa Island", "Nepal", "Nicaragua", "Níger", "Nigeria", "Niue", "Noruega", "Nueva Caledonia", "Nueva Zelanda", "Omán", "Pacific Ocean", "Países Bajos", "Pakistán", "Palaos", "Panamá", "Papúa-Nueva Guinea", "Paracel Islands", "Paraguay", "Perú", "Polinesia Francesa", "Polonia", "Portugal", "Puerto Rico", "Qatar", "Reino Unido", "República Centroafricana", "República Checa", "República Democrática del Congo", "República Dominicana", "Ruanda", "Rumania", "Rusia", "Sáhara Occidental", "Samoa", "Samoa Americana", "San Cristóbal y Nieves", "San Marino", "San Pedro y Miquelón", "San Vicente y las Granadinas", "Santa Helena", "Santa Lucía", "Santo Tomé y Príncipe", "Senegal", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Southern Ocean", "Spratly Islands", "Sri Lanka", "Suazilandia", "Sudáfrica", "Sudán", "Suecia", "Suiza", "Surinam", "Svalbard y Jan Mayen", "Tailandia", "Taiwán", "Tanzania", "Tayikistán", "TerritorioBritánicodel Océano Indico", "Territorios Australes Franceses", "Timor Oriental", "Togo", "Tokelau", "Tonga", "Trinidad y Tobago", "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Unión Europea", "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Wake Island", "Wallis y Futuna", "West Bank", "World", "Yemen", "Yibuti", "Zambia", "Zimbabue"]  

PAISES=[[x,x] for x in COUNTRIES]

GENEROS= (
	('Masculino','Masculino'),
	('Femenino', 'Femenino'),
	('Otros', 'Otros'),
	)

years=[i for i in range(1930,2010)]


months= {
    1: ('Enero'), 2: ('Febrero'), 3: ('Marzo'), 4: ('Abril'), 5: ('Mayo'), 6: ('Junio'),
    7: ('Julio'), 8: ('Agosto'), 9: ('Septiembre'), 10: ('Octubre'), 11: ('Noviembre'),
    12: ('Dieciembre')
}

class RegistroForm(forms.Form):

    nombres = forms.CharField(label="Nombres", required=True, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tus nombres'}
    ), max_length=100)

    apellidos = forms.CharField(label="Apellidos", required=True, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tus apellidos', 'id':'app'}
    ), max_length=100)

    pais = forms.CharField(label="Pais", required=True, widget= forms.Select(choices=PAISES)) 
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento",required =False, widget=forms.SelectDateWidget(months=months, years=years, empty_label=("Año", "Mes", "Día"),)) #campo opcional 
    email = forms.EmailField(label="Email",required=True, widget=forms.EmailInput(
        attrs= {'class':'form-control', 'placeholder':'Escribe tu email'}), max_length=100, min_length=3) #campo opcional
    
    genero= forms.CharField(label="Generos", required=False, widget= forms.Select(choices=GENEROS)) 
    

    contraseña = forms.CharField(label="Contraseña", required=True, widget= forms.PasswordInput()) 

    captcha = ReCaptchaField(public_key = '6LdaUqcUAAAAAOK3xzjo-oknTM33fbXExlcwFG0z',private_key = '6LdaUqcUAAAAANtBkskWrDSPz2SezQT_i3jsSRon', widget= ReCaptchaV2Checkbox())

    def clean_nombres(self):
        nombres = self.cleaned_data['nombres']
        if not nombres.isalpha():
            raise forms.ValidationError('Introduce un nombre valido')            
        return nombres;    

    def clean_apellidos(self):
        apellidos = self.cleaned_data['apellidos']
        if not apellidos.isalpha():
            raise forms.ValidationError('Introduce un apellido valido')            
        return apellidos


    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@utp.edu.co'):
            raise forms.ValidationError('El email debe ser @utp.edu.co')  
        else:
            if Egresado.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya esta registrado, prueba con otro')
        return email

    def clean_contraseña(self):
        contraseña= self.cleaned_data['contraseña']
        if contraseña.isdigit():
            raise forms.ValidationError('Su contraseña no puede ser completamente numérica')
        elif len(contraseña)<8:
            raise forms.ValidationError('Su contraseña debe tener al menos 8 caracteres')
        return contraseña


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder': 'Biografia'})
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y deve ser válido")

    class Meta:
        model = Egresado
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        
        if 'email' in self.changed_data:  #es una liasta que almacena todos los campos que se han editado en el formulario            
            if not email.endswith('@utp.edu.co'):
                raise forms.ValidationError('El email debe ser @utp.edu.co')  
            else:
                if Egresado.objects.filter(email=email).exists():
                    raise forms.ValidationError('El email ya esta registrado, prueba con otro')
        return email