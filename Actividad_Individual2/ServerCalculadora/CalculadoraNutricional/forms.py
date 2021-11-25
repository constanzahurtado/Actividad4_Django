from django import forms
from django.db.models import fields
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('rut','nombre','apellido','email', 'genero', 'edad')