# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_auto_20151013_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='quantidade',
            field=models.CharField(max_length=16, blank=True),
        ),
    ]
