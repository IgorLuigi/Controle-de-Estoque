from django.urls import path

from.views import EstadoCreate, CidadeCreate, ClienteCreate, FornecedorCreate, FuncionarioCreate, ProdutoCreate, VendasCreate
from.views import EstadoUpdate, CidadeUpdate, ClienteUpdate, FornecedorUpdate, FuncionarioUpdate, ProdutoUpdate, VendasUpdate

urlpatterns = [

  path('cadastrar/estado/', EstadoCreate.as_view(), name="cadastrar-estado"),
  path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
  path('cadastrar/cliente/', ClienteCreate.as_view(), name="cadastrar-cliente"),
  path('cadastrar/fornecedor/', FornecedorCreate.as_view(), name="cadastrar-fornecedor"),
  path('cadastrar/funcionario/', FuncionarioCreate.as_view(), name="cadastrar-funcionario"),
  path('cadastrar/produto/', ProdutoCreate.as_view(), name="cadastrar-produto"),
  path('cadastrar/venda/', VendasCreate.as_view(), name="cadastrar-venda"),


  path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
  path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
  path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
  path('editar/fornecedor/<int:pk>/', FornecedorUpdate.as_view(), name='editar-fornecedor'),
  path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
  path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),
  path('editar/venda/<int:pk>/', VendasUpdate.as_view(), name='editar-venda'),

  
   
]