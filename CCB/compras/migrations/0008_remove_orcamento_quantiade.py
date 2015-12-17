# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_auto_20150822_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento',
            name='quantiade',
        ),
    ]
