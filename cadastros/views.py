from typing import List
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from.models import Estado, Cidade, Cliente, Funcionario, Fornecedor, Produtos, Vendas

from django.urls import reverse_lazy

# Create your views here.

class EstadoCreate(CreateView):
    model = Estado
    fields = ['nomeestado', 'sigla']
    templates_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nomecidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nomecliente', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nomefuncionario', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionarios')

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['nomefornecedor', 'cnpj', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

class ProdutoCreate(CreateView):
    model = Produtos
    fields = ['nomeproduto', 'marca', 'teste', 'dataproducao', 'datavalidade', 'preco', 'datacadastro', 'status', 'fornecedor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

class VendasCreate(CreateView):
    model = Vendas
    fields = ['quantidade', 'precototal', 'datavenda', 'status', 'cliente', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-vendas')

################ UPDATE ###########################################################################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nomeestado', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nomecidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nomecliente', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nomefuncionario', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionarios')

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nomefornecedor', 'cnpj', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

class ProdutoUpdate(UpdateView):
    model = Produtos
    fields = ['nomeproduto', 'marca', 'teste', 'dataproducao', 'datavalidade', 'preco', 'datacadastro', 'status', 'fornecedor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

class VendasUpdate(UpdateView):
    model = Vendas
    fields = ['quantidade', 'precototal', 'datavenda', 'status', 'cliente', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-vendas')

################ DELETE ###########################################################################

class EstadoDelete(DeleteView):
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionarios')

class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedores')

class ProdutoDelete(DeleteView):
    model = Produtos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')

class VendasDelete(DeleteView):
    model = Vendas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-vendas')

################ LIST ###########################################################################

class EstadoList(ListView): 
    model = Estado
    template_name = 'cadastros/listar/estado.html'

class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listar/cidade.html'

class ClienteList(ListView):
    model = Cliente
    template_name = 'cadastros/listar/cliente.html'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listar/funcionario.html'

class FornecedorList(ListView):
    model = Fornecedor
    template_name = 'cadastros/listar/fornecedor.html'

class ProdutoList(ListView):
    model = Produtos
    template_name = 'cadastros/listar/produtos.html'

class VendasList(ListView):
    model = Vendas
    template_name = 'cadastros/listar/vendas.html'
