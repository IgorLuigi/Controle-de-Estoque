from typing import List
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from.models import Estado, Cidade, Cliente, Funcionario, Fornecedor, Produtos, Vendas

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

# Create your views here.

class EstadoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Estado
    fields = ['nomeestado', 'sigla']
    template_name = 'cadastros/form.html'
<<<<<<< HEAD
    success_url = reverse_lazy('listar-estado')
=======
    success_url = reverse_lazy('listar-estados')
>>>>>>> b2d77237b0ea68d79d566d466a0fd0b7d8f4d498

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Estados"

        return context


class CidadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cidade
    fields = ['nomecidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Cidades"

        return context

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nomecliente', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Clientes"

        return context

class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Funcionario
    fields = ['nomefuncionario', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionarios')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Funcionários"

        return context

class FornecedorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fornecedor
    fields = ['nomefornecedor', 'cnpj', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Fornecedores"

        return context

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produtos
    fields = ['nomeproduto', 'marca', 'dataproducao', 'datavalidade', 'preco', 'datacadastro', 'status', 'fornecedor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Produtos"

        return context

class VendasCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Vendas
    fields = ['quantidade', 'precototal', 'datavenda', 'status', 'cliente', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-vendas')

    def form_valid(self, form):
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Vendas"

        return context

################ UPDATE ###########################################################################

class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nomeestado', 'sigla']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estados')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Estados"

        return context

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nomecidade', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Cidades"

        return context

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nomecliente', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-clientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Clientes"

        return context

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nomefuncionario', 'cpf', 'rg', 'email', 'telefone', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionarios')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Funcionários"

        return context

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['nomefornecedor', 'cnpj', 'endereco', 'datacadastro', 'status', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-fornecedores')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Fornecedores"

        return context

class ProdutoUpdate(UpdateView):
    model = Produtos
    fields = ['nomeproduto', 'marca', 'dataproducao', 'datavalidade', 'preco', 'datacadastro', 'status', 'fornecedor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Produtos"

        return context

class VendasUpdate(UpdateView):
    model = Vendas
    fields = ['quantidade', 'precototal', 'datavenda', 'status', 'cliente', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-vendas')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Vendas"

        return context

################ DELETE ###########################################################################

class EstadoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Estado
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-estados')

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

class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
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

class FuncionarioList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
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
