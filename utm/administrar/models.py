from django.db import models

# Create your models here.

class materiales(models.Model): #Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=30,verbose_name="Matricula") #Texto corto
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo")
    carrera = models.CharField(max_length=50,verbose_name="Carrera")
    practica = models.CharField(max_length=40, verbose_name="Nombre Practica")
    materiales = models.TextField(verbose_name="Materiales") #Texto largo
    cantidad = models.IntegerField(verbose_name="Cantidad")
    precio = models.DecimalField(max_digits=6,decimal_places=2,default=00.00 ,verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al mas viejo
    def __str__(self):
        return self.nombre 
        #Indica que se mostrára el nombre como valor en la tabla

class Empleados(models.Model): #Define la estructura de nuestra tabla
    nombre = models.CharField(max_length=30,verbose_name="Nombre") #Texto largo
    correo = models.EmailField(verbose_name="Correo")
    telefono = models.CharField(max_length=10,verbose_name="Telefono")
    area = models.CharField(max_length=25,verbose_name="Area")
    cargo = models.CharField(max_length=30,verbose_name="Cargo")
    turno = models.CharField(max_length=10)
    actividades = models.TextField(verbose_name="Actividades")
    imagen = models.ImageField(null=True,upload_to="fotos empleados",verbose_name="Fotografía")
    
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al mas viejo
    def __str__(self):
        return self.nombre 
        #Indica que se mostrára el nombre como valor en la tabla

class noticias(models.Model): #Define la estructura de nuestra tabla
    titulo = models.CharField(max_length=60,verbose_name="Nombre") #Texto largo
    descripcion = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(null=True,upload_to="fotosnoticias",verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True) #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al mas viejo
    def __str__(self):
        return self.titulo 
        #Indica que se mostrára el nombre como valor en la tabla
