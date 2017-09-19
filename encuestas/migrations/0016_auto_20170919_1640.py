# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0015_auto_20170502_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animales',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animales'},
        ),
        migrations.AddField(
            model_name='animales',
            name='unidad_medida',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
