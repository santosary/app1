# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20150726_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ManyToManyField(to='compras.Fornecedor'),
            preserve_default=True,
        ),
    ]
