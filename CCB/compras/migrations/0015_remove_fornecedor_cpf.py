# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0014_auto_20151111_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='cpf',
        ),
    ]
