# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_remove_orcamento_quantiade'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='medida',
            field=models.ForeignKey(default=0, to='compras.Un_medida'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='preco_atacado',
            field=models.DecimalField(default=1992, max_digits=10, decimal_places=2, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='quantidade',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_prazo',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='preco_vista',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
