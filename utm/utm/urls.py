"""utm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from administrar import views
from registros import views as views_registros
from django.conf import settings 
#permite acceder a las variables MEDIA_URL y MEDIA_ROOT que almacenan la ubicación de nuestras imagenes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal,name="Principal"),
    path('materiales/',views.vistamateriales,name="Materiales"),
    path('agregar material/',views.form_material,name="FormMateriales"),
    path('registrar material/',views.registrar_material,name="RegistrarMaterial"),
    path('EliminarMaterial/<int:id>/',views.eliminarMaterial,name="EliminarMaterial"),
    path('formEditarMaterial/<int:id>/', views.consultarMaterialIndividual, name='ConsultarMaterialIndividual'),
    path('guardarEdicionMateria/<int:id>/', views.guardaredicionMaterial, name='GuardarEdicionMateria'),
    path('noticias/',views.noticiasvista,name="Noticias"),
    path('subirnoticia/',views.subirnoticia,name="SubirNoticia"),
    path('eliminarnoticia/<int:id>/', views.EliminarNoticia, name='EliminarNoticia'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
