from django.urls import path

from.views import EstadoCreate, CidadeCreate, ClienteCreate, FornecedorCreate, FuncionarioCreate, ProdutoCreate, VendasCreate
from.views import EstadoUpdate, CidadeUpdate, ClienteUpdate, FornecedorUpdate, FuncionarioUpdate, ProdutoUpdate, VendasUpdate
from.views import EstadoDelete, CidadeDelete, ClienteDelete, FornecedorDelete, FuncionarioDelete, ProdutoDelete, VendasDelete
from.views import EstadoList, CidadeList, ClienteList, FornecedorList, FuncionarioList, ProdutoList, VendasList

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
  path('editar/venda/<int:pk>/', VendasUpdate.as_view(), name='editar-vendas'),


  path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),
  path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
  path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
  path('excluir/fornecedor/<int:pk>/', FornecedorDelete.as_view(), name='excluir-fornecedor'),
  path('excluir/funcionario/<int:pk>/', FuncionarioDelete.as_view(), name='excluir-funcionario'),
  path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),
  path('excluir/venda/<int:pk>/', VendasDelete.as_view(), name='excluir-vendas'),

  
  path('listar/estado/', EstadoList.as_view(), name='listar-estado'),
  path('listar/cidade/', CidadeList.as_view(), name='listar-cidades'),
  path('listar/cliente/', ClienteList.as_view(), name='listar-clientes'),
  path('listar/fornecedor/', FornecedorList.as_view(), name='listar-fornecedores'),
  path('listar/funcionario/', FuncionarioList.as_view(), name='listar-funcionarios'),
  path('listar/produto/', ProdutoList.as_view(), name='listar-produtos'),
  path('listar/venda/', VendasList.as_view(), name='listar-vendas'),
  
   
]