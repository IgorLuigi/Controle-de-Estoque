from django.contrib import admin

# Import de Classes
from .models import Estado, Cidade, Cliente, Funcionario, Fornecedor

# Register your models here.

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Fornecedor)