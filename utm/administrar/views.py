from django.shortcuts import render, HttpResponse
from .models import materiales,noticias
from .models import materiales
from .forms import MaterialesForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import FormNoticia
# Create your views here.
def principal(request):
    noticia=noticias.objects.all()
    return render(request,"administrar/principal.html",{'noticias':noticia})

def vistamateriales(request):
    material=materiales.objects.all()
    numeroregistros=materiales.objects.all().count()
    if(numeroregistros == 0):
        return render(request,"administrar/materialesvacio.html",{'numero':numeroregistros})
    else:
        return render(request,"administrar/materiales.html",{'materiales':material})
    

    #Indicamos el lugar donde se renderizará el resultado de esta vista

def form_material(request):
    return render(request,"administrar/formulario_materiales.html")

def registrar_material(request):
    if request.method == 'POST':
        form = MaterialesForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            materiale=materiales.objects.all()
            numeroregistros=materiales.objects.all().count()
            if(numeroregistros == 0):
                return render(request,"administrar/materialesvacio.html",{'numero':numeroregistros})
            else:
                return render(request,"administrar/materiales.html",{'materiales':materiale})
        #return render(request,'administrar/formulario_materiales.html') 
    form = MaterialesForm()
        #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'administrar/formulario_materiales.html',{'form': form}) 

def eliminarMaterial(request, id, confirmacion='administrar/confirmareliminacion.html'):
    materia = get_object_or_404(materiales, id=id)
    if request.method=='POST':
        materia.delete()
        material=materiales.objects.all()
        numeroregistros=materiales.objects.all().count()
        if(numeroregistros == 0):
            return render(request,"administrar/materialesvacio.html",{'numero':numeroregistros})
        else:
            return render(request,"administrar/materiales.html",{'materiales':material})
       
    return render(request, confirmacion, {'object':materia})

def consultarMaterialIndividual(request, id):
    material=materiales.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objetos 
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que coincide con su
    #consulta.
    return render(request,"administrar/formEditarMateriales.html",{'material':material})

def guardaredicionMaterial(request, id):
    material = get_object_or_404(materiales, id=id)
    form = MaterialesForm(request.POST, instance=material)
    #Referenciamos que el elemento del formulario pertenece al comentario 
    # ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica. 
        materiale=materiales.objects.all()
        numeroregistros=materiales.objects.all().count()
        if(numeroregistros == 0):
            return render(request,"administrar/materialesvacio.html",{'numero':numeroregistros})
        else:
            return render(request,"administrar/materiales.html",{'materiales':materiale})
            return render(request,"administrar/materiales.html",{'materiales':materiale})
    #Si el formurio no es valido nos regresa al formulario para verificar
    #datos
    return render(request,"administrar/formEditarMateriales.html",{'material':material})

def noticiasvista(request):
    noticia=noticias.objects.all()
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request,"administrar/noticias.html",{'noticias':noticia})

def subirnoticia(request):
    if request.method == 'POST':
        form = FormNoticia(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            noticia=noticias.objects.all()
            return render(request,"administrar/principal.html",{'noticias':noticia})
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        noticia=noticias.objects.all()
        return render(request,"administrar/principal.html",{'noticias':noticia})

def EliminarNoticia(request, id, confirmacion='administrar/confirmarEliminacionNoticia.html'):
    comentario = get_object_or_404(noticias, id=id)
    if request.method=='POST':
        comentario.delete()
        noticia=noticias.objects.all()
        return render(request,"administrar/principal.html",{'noticias':noticia})
    return render(request, confirmacion, {'object':comentario})