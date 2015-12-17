# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0013_auto_20151013_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cpf',
            field=models.CharField(default=b'000.000.000-00', max_length=14, blank=True),
        ),
    ]
