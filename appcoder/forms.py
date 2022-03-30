
from django import forms

class PosteoFormulario(forms.Form):

    # Campos del formulario
    titulo = forms.CharField(max_length=40) # Campo con restricciones
    texto = forms.IntegerField()