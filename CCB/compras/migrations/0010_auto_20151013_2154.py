# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20151013_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='fornecedor',
            field=models.ForeignKey(to='compras.Fornecedor'),
        ),
    ]
