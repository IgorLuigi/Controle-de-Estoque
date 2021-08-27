from re import VERBOSE
from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor

# Create your models here.
# class Campo(models.Model):
#     nome = models.CharField(max_length=50)
#     descricao = models.CharField(max_length=150, verbose_name="Descrição")

#     def __str__(self):
#         return "{} ({})".format(self.nome, self.descricao)

# class Atividade(models.Model):
#     numero = models.IntegerField(verbose_name="Número")
#     descricao = models.CharField(max_length=150, verbose_name="Descrição")
#     pontos = models.DecimalField(decimal_places=1, max_digits=4)
#     detalhes = models.CharField(max_length=100)

#     campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

#     def __str__(self):
#         return "{} ({})".format(self.nome, self.campo)

class Estado(models.Model):
    nomeestado = models.CharField(max_length=30, verbose_name="Estado")
    sigla = models.CharField(max_length=2, verbose_name="Sigla")

    def __str__(self):
        return "{} ({})".format(self.nomeestado, self.sigla)

class Cidade(models.Model):
    nomecidade = models.CharField(max_length=50, verbose_name="Cidade")

    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.nomecidade, self.estado.sigla) 

class Cliente(models.Model):
    nomecliente = models.CharField(max_length=50, verbose_name="Cliente")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=12, verbose_name="RG")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefone = models.CharField(max_length=12, verbose_name="Telefone")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    datacadastro = models.DateField(verbose_name="Data de Cadastro")
    status = models.CharField(max_length=1, verbose_name="Status")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nomecliente)

class Funcionario(models.Model):
    nomefuncionario = models.CharField(max_length=50, verbose_name="Funcionário")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    rg = models.CharField(max_length=12, verbose_name="RG")
    email = models.CharField(max_length=100, verbose_name="Email")
    telefone = models.CharField(max_length=12, verbose_name="Telefone")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    datacadastro = models.DateField(verbose_name="Data de Cadastro")
    status = models.CharField(max_length=1, verbose_name="Status")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nomefuncionario)

class Fornecedor(models.Model):
    nomefornecedor = models.CharField(max_length=50, verbose_name="Fornecedor")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    datacadastro = models.DateField(verbose_name="Data de Cadastro")
    status = models.CharField(max_length=1, verbose_name="Status")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.nomefornecedor)

class Produtos(models.Model):
    nomeproduto = models.CharField(max_length=50, verbose_name="Produto")
    marca = models.CharField(max_length=30, verbose_name="Marca")
    dataproducao = models.DateField(verbose_name="Data Produção")
    datavalidade = models.DateField(verbose_name="Data Validade")
    preco = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Preço")
    datacadastro = models.DateField(verbose_name="Data Cadastro")
    status = models.CharField(max_length=1, verbose_name="Status")

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    
    def __str__(self):
        return "{}".format(self.nomeproduto)

class Vendas(models.Model):
    quantidade = models.IntegerField(verbose_name="Quantidade")
    precototal = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Preço Total")
    datavenda = models.DateField(verbose_name="Data Venda")
    status = models.CharField(max_length=1, verbose_name="Status")

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({})".format(self.datavenda, self.cliente.nome)