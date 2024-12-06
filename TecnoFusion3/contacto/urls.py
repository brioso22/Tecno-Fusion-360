from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactanos, name='contactanos'),
]
