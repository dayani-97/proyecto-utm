from django.contrib import admin
from .models import materiales
from .models import Empleados,noticias

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera','practica')
    search_fields = ('matricula','nombre','carrera','practica')
    date_hierarchy = 'created'
    list_filter = ('carrera','practica')
    list_per_page=4
    list_display_links=('matricula','nombre')
admin.site.register(materiales,AdministrarModelo)

class AdministrarModeloEmpleado(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('correo', 'nombre', 'area','turno')
    search_fields = ('correo','nombre','area','turno')
    date_hierarchy = 'created'
    list_filter = ('cargo','area','turno')
    list_per_page=4
    list_display_links=('correo','nombre')
admin.site.register(Empleados,AdministrarModeloEmpleado)

admin.site.register(noticias)

