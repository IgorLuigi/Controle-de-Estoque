from typing import List
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from.models import Estado, Cidade, Cliente, Funcionario, Fornecedor, Produtos, Vendas

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nomeestado', 'sigla']
    templates_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nomecidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nomecliente', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

class FuncionarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Funcionario
    fields = ['nomefuncionario', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionarios')

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nomefornecedor', 'cnpj', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produtos
    fields = ['nomeproduto', 'marca', 'teste', 'dataproducao', 'datavalidade', 'preco', 'datacadastro', 'status', 'fornecedor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

class VendasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
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

class EstadoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estado')

class CidadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')

class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-clientes')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-funcionarios')

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-fornecedores')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produtos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')

class VendasDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Vendas
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-vendas')

################ LIST ###########################################################################

class EstadoList(LoginRequiredMixin, ListView): 
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'cadastros/listar/estado.html'

class CidadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cidade
    template_name = 'cadastros/listar/cidade.html'

class ClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/listar/cliente.html'

class FuncionarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    template_name = 'cadastros/listar/funcionario.html'

class FornecedorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    template_name = 'cadastros/listar/fornecedor.html'

class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produtos
    template_name = 'cadastros/listar/produtos.html'

class VendasList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Vendas
    template_name = 'cadastros/listar/vendas.html'
