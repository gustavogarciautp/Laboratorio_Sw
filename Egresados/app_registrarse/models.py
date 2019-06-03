from django.db import models

class Registrarse (models.Model):
    #DNI = models.CharField(primary_key=True, max_length=20)
    nombres =models.CharField(verbose_name= "Nombres", max_length=30, blank= False, null=False)
    apellidos = models.CharField(verbose_name= "Apellidos", default='',max_length=30, blank= False, null=False)
    pais = models.CharField(verbose_name="Pais",default='',null= False, blank= False, max_length=30) #campo opcional
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento",null= True, blank= True) #campo opcional
    email = models.EmailField(verbose_name="Email",default='',null= False, blank= False, unique=True) #campo opcional
    genero = models.CharField(verbose_name="Genero",default='',null= True, blank= True, max_length=10) #campo opcional
    contraseña = models.CharField(verbose_name="Contraseña",default='',null= False, blank= False, max_length=50) #campo opcional
    activacion = models.BooleanField(verbose_name="activacion",default=False, null= False, blank= False) #campo opcional

    class Meta:
        verbose_name = 'Egresado'
        verbose_name_plural= 'Egresados'
        #ordering = ['order','title']

    def __str__(self):
        return self.nombres