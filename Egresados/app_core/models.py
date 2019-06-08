from django.db import models

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
    12: ('Diciembre')
}

class Usuario(models.Model):
    REQUIRED_FIELDS = ('email','contraseña')
    nombres =models.CharField(verbose_name= "Nombres", max_length=30, blank= False, null=False)
    apellidos = models.CharField(verbose_name= "Apellidos", default='',max_length=30, blank= False, null=False)
    pais = models.CharField(verbose_name="Pais",default='',null= False, blank= False, max_length=30, choices=PAISES) #campo opcional
    email = models.EmailField(verbose_name="Email",default='',null= False, blank= False, unique=True) #campo opcional
    genero = models.CharField(verbose_name="Genero",default='',null= True, blank= True, max_length=10, choices=GENEROS) #campo opcional
    contraseña = models.CharField(verbose_name="Contraseña",default='',null= False, blank= False, max_length=50) #campo opcional
    id_restablecimiento = models.CharField(verbose_name="Id Recuperacion", default='', null=True, blank=True, max_length=60)
    #telefono = models.IntegerField(verbose_name= "Telefono", default='', null=True, max_length=20, min_length=10)
    #direccion = models.CharField(verbose_name= "Direccion", max_length=30, blank= False, null=False)
    #ciudad= models.CharField(verbose_name= "Ciudad", max_length=30, blank= False, null=False)	
    USERNAME_FIELD='email'

class SuperUser (Usuario):
    telefono = models.IntegerField(verbose_name= "Telefono", default='', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Superusuario'
        verbose_name_plural= 'Superusuario'
        #ordering = ['order','title']

    def __str__(self):
        return self.nombres


class Administrador (Usuario):
    telefono = models.IntegerField(verbose_name= "Telefono", default='', null=True, blank=True)
    direccion = models.CharField(verbose_name= "Direccion", max_length=30, blank= False, null=False)
    ciudad= models.CharField(verbose_name= "Ciudad", max_length=30, blank= False, null=False)
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural= 'Administradores'
        #ordering = ['order','title']

    def __str__(self):
        return self.nombres

class Egresado (Usuario):
    activacion= models.BooleanField(verbose_name= "Activacion", default= False, null=True, blank= False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento",null= True, blank= True) #campo opcional
 
    class Meta:
        verbose_name = 'Egresado'
        verbose_name_plural= 'Egresados'
        #ordering = ['order','title']

    def activate(self):
        return self.activacion

    def __str__(self):
        return self.nombres


class Interes(models.Model):
    nombre = models.CharField(verbose_name= "Nombre", default='', null=True, blank= False, max_length=30)

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural= 'Interes'


class Intereses(models.Model):
    interes = models.ForeignKey(Interes, on_delete=models.CASCADE)
    egresado= models.ForeignKey(Egresado, on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'Intereses'
        verbose_name_plural= 'Intereses'
