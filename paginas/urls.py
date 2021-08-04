from django.urls import path
from .views import PaginaInicial

urlpatterns = [
     # path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('', PaginaInicial.as_view(), name='index'), 
   
]