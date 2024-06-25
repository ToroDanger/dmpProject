from django import forms
from .models import Inicio

from django.forms import ModelForm

class Inicioform(ModelForm):
    class Meta:
        model=Inicio
        fields= "__all__"
