from django.urls import path
from . import views

urlpatterns = [
    path('', views.donaciones, name='donaciones'),
    path('registrar-donacion/', views.registrar_donacion, name='registrar_donacion'),
]