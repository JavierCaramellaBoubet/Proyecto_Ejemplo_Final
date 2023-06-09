"""proyectoejemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from proyectoejemplo.views import saludar # Podemos importar de a un controlador o como vemos debajo TODOS JUNTOS
# from proyectoejemplo.views import segunda_vista
from proyectoejemplo.views import * # Para importar todos los controladores



urlpatterns = [
    path('admin/', admin.site.urls),
    path ('saludar/', saludar),
    path('segunda/', segunda_vista),
    path('dia/', dia_de_hoy),
    path('saludo/ <nombre>', saludo_con_nombre),
    path('anio/<edad>', calcula_anio_nacimiento),
    path('probandoHtml', probandoHtml),
]
