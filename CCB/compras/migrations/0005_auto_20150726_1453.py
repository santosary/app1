# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20150723_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='claro',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='contato',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='fixo',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='oi',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='referencia',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='tim',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='vivo',
        ),
        migrations.AddField(
            model_name='endereco',
            name='claro',
            field=models.CharField(default=b'(38)-', max_length=14),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='contato',
            field=models.CharField(default=-2010, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='email',
            field=models.EmailField(default=-1996, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='fixo',
            field=models.CharField(default=b'(38)-', max_length=13),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='oi',
            field=models.CharField(default=b'(38)-', max_length=14),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='referencia',
            field=models.CharField(default=-19, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='tim',
            field=models.CharField(default=b'(38)-', max_length=14),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='vivo',
            field=models.CharField(default=b'(38)-', max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_prazo',
            field=models.DecimalField(max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_vista',
            field=models.DecimalField(max_digits=10, decimal_places=2, blank=True),
        ),
    ]
