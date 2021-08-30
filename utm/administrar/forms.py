from django import forms
from .models import materiales,noticias
from django.forms import ModelForm, ClearableFileInput


class MaterialesForm(forms.ModelForm):
    class Meta:
        model = materiales
        fields = ['matricula','nombre','correo','carrera','practica','materiales','cantidad','precio']


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormNoticia(ModelForm):
    class Meta:
        model = noticias
        fields = ('titulo', 'descripcion', 'imagen')
        widgets = {
        'imagen': CustomClearableFileInput
        }
