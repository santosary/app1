# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='quantiade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categria',
            name='descricao',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='claro',
            field=models.CharField(default=b'(38)', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(default=b'00.000.000/0001-97', max_length=18),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cpf',
            field=models.CharField(default=b'000.000.000-00', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='fixo',
            field=models.CharField(default=b'(38)', max_length=13),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome_fantasia',
            field=models.CharField(unique=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='oi',
            field=models.CharField(default=b'(38)', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='razao_social',
            field=models.CharField(unique=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='tim',
            field=models.CharField(default=b'(38)', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='vivo',
            field=models.CharField(default=b'(38)', max_length=24),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='qt_parcelas',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='un_medida',
            name='descricao',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
