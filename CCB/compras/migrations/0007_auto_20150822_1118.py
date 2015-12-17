# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_produto_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='claro',
            field=models.CharField(default=b'(38)0000-0000', max_length=14),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='fixo',
            field=models.CharField(default=b'(38)3000-0000', max_length=13),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='oi',
            field=models.CharField(default=b'(38)0000-0000', max_length=14),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='tim',
            field=models.CharField(default=b'(38)0000-0000', max_length=14),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='vivo',
            field=models.CharField(default=b'(38)0000-0000', max_length=24),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(default=b'00.000.000/0001-97', unique=True, max_length=18),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cpf',
            field=models.CharField(default=b'000.000.000-00', unique=True, max_length=14),
        ),
    ]
