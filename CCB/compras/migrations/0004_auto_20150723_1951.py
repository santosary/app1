# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20150711_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='endereco',
        ),
        migrations.AddField(
            model_name='endereco',
            name='fornecedor',
            field=models.ForeignKey(default=1, to='compras.Fornecedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_prazo',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_vista',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
