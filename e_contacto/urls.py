from django.urls import path
from .views import render_contacto

app_name = 'e_contacto'

urlpatterns = [
    path('', render_contacto, name='contacto')
]