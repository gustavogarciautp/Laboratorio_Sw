from django.contrib import admin

# Register your models here.
from .models import Egresado, Administrador, SuperUser, Intereses, Interes

class EgresadoAdmin(admin.ModelAdmin):
	exclude= ('id_restablecimiento',)

admin.site.register(Administrador)
admin.site.register(Egresado, EgresadoAdmin)
admin.site.register(SuperUser)

admin.site.register(Interes)
admin.site.register(Intereses)
