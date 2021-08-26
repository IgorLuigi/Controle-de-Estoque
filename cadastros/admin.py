from django.contrib import admin

# Import de Classes
from .models import Estado, Cidade, Cliente, Funcionario, Fornecedor, Produtos, Vendas

# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Fornecedor)
admin.site.register(Produtos)
admin.site.register(Vendas)