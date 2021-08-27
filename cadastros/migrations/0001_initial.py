# Generated by Django 2.2.12 on 2021-08-27 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecidade', models.CharField(max_length=50, verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecliente', models.CharField(max_length=50, verbose_name='Cliente')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(max_length=12, verbose_name='RG')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('datacadastro', models.DateField(verbose_name='Data de Cadastro')),
                ('status', models.CharField(max_length=1, verbose_name='Status')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeestado', models.CharField(max_length=30, verbose_name='Estado')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomefornecedor', models.CharField(max_length=50, verbose_name='Fornecedor')),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('datacadastro', models.DateField(verbose_name='Data de Cadastro')),
                ('status', models.CharField(max_length=1, verbose_name='Status')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomefuncionario', models.CharField(max_length=50, verbose_name='Funcionário')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(max_length=12, verbose_name='RG')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('telefone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('datacadastro', models.DateField(verbose_name='Data de Cadastro')),
                ('status', models.CharField(max_length=1, verbose_name='Status')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('precototal', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço Total')),
                ('datavenda', models.DateField(verbose_name='Data Venda')),
                ('status', models.CharField(max_length=1, verbose_name='Status')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeproduto', models.CharField(max_length=50, verbose_name='Produto')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('dataproducao', models.DateField(verbose_name='Data Produção')),
                ('datavalidade', models.DateField(verbose_name='Data Validade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('datacadastro', models.DateField(verbose_name='Data Cadastro')),
                ('status', models.CharField(max_length=1, verbose_name='Status')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Fornecedor')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Estado'),
        ),
    ]
