from django.urls import path, include
from src.views import index, bom_samaritano, doacoes, voluntarios, contato

urlpatterns = [
    path('', index),
    path('bom-samaritano', bom_samaritano),
    path('doacoes', doacoes),
    path('voluntarios', voluntarios),
    path('contato', contato),
]
