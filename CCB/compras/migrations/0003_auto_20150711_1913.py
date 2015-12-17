# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20150711_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='claro',
            field=models.CharField(default=b'(38)-', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='fixo',
            field=models.CharField(default=b'(38)-', max_length=13),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='oi',
            field=models.CharField(default=b'(38)-', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='tim',
            field=models.CharField(default=b'(38)-', max_length=14),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='vivo',
            field=models.CharField(default=b'(38)-', max_length=24),
        ),
    ]
