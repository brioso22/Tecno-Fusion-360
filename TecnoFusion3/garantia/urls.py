from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_garantia, name='formulario_garantia'),  # Define la URL con el nombre correcto
]
