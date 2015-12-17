# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=40)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
                ('uf', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_fantasia', models.CharField(max_length=80)),
                ('razao_social', models.CharField(max_length=80)),
                ('cnpj', models.CharField(max_length=18)),
                ('cpf', models.CharField(max_length=14)),
                ('contato', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=75)),
                ('fixo', models.CharField(max_length=13)),
                ('tim', models.CharField(max_length=14)),
                ('vivo', models.CharField(max_length=24)),
                ('claro', models.CharField(max_length=14)),
                ('oi', models.CharField(max_length=14)),
                ('referencia', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(to='compras.Endereco')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('preco_vista', models.DecimalField(max_digits=10, decimal_places=2)),
                ('preco_prazo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('qt_parcelas', models.IntegerField()),
                ('fornecedor', models.OneToOneField(to='compras.Fornecedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(to='compras.Categria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Un_medida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='produto',
            name='un_medida',
            field=models.ManyToManyField(to='compras.Un_medida'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='produto',
            field=models.ForeignKey(to='compras.Produto'),
            preserve_default=True,
        ),
    ]
