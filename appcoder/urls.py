from unicodedata import name
from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('posteos/', posteos, name="Posteos"),    
    path('buscarposteo/', buscar_posteo, name='BuscarPosteo'),
    path('paises/', paises, name="Paises"),    
    path('ciudades/', ciudades, name="Ciudades"),    

]
