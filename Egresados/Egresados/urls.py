"""Egresados URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app_core import views as app_core_views  #importamos de nuestra app core el fichero views
from app_registrarse import views as app_registrarse_views
from django.conf import settings

urlpatterns = [
	path('login/', app_core_views.login, kwargs= {'vista': 'egresado'}, name='login'),
    path('ad-min/', app_core_views.login, kwargs= {'vista': 'administradpr'},name='admin'),
	path('registrarse/', app_registrarse_views.registrarse, name='registrarse'),
    path('recuperar_1/', app_core_views.recuperar_1, name='recuperar_1'),
    path('recuperar_2/', include('app_core.urls')),
    path('principal/', app_core_views.principal, name='principal'),
    #path('recuperar_2', app_core_views.recuperar_2, name='recuperar_2'),
    path('super-user/', admin.site.urls),
    path('perfil/', app_registrarse_views.ProfileUpdate.as_view(), name='perfil')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)