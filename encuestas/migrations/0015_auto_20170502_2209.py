# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0014_encuesta_estacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostoGanaderia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(verbose_name=b'Costo total en Moneda local')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Costo para ganaderia mayor y menor',
            },
        ),
        migrations.CreateModel(
            name='CostoProcesamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('costo', models.FloatField(verbose_name=b'Costo total en Moneda local')),
                ('encuesta', models.ForeignKey(to='encuestas.Encuesta')),
            ],
            options={
                'verbose_name_plural': 'Costo para productos procesados',
            },
        ),
        migrations.AlterModelOptions(
            name='costofrutas',
            options={'verbose_name_plural': 'Total Mz y costo para frutas familiar'},
        ),
        migrations.AddField(
            model_name='cultivostradicionales',
            name='precio_consumido',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='distribuciontierra',
            name='tierra',
            field=models.IntegerField(verbose_name=b'20.1_Distribuci\xc3\xb3n de la tierra en la finca', choices=[(1, b'Bosque'), (2, b'Tacotal/Guamil/Machorra/Llano'), (3, b'Cultivo anual'), (4, b'Plantaci\xc3\xb3n forestal'), (5, b'Potrero'), (6, b'Pasto en asocio con \xc3\xa1rboles'), (7, b'Frutales'), (8, b'Cultivos en asocio')]),
        ),
        migrations.AlterField(
            model_name='duenono',
            name='no',
            field=models.IntegerField(choices=[(1, b'Arrendada'), (2, b'Promesa de venta'), (3, b'Prestada'), (4, b'Tierra Ind\xc3\xadgena/Comunal'), (5, b'Sin escritura'), (6, b'Colectivo/Cooperativa')]),
        ),
        migrations.AlterField(
            model_name='entrevistados',
            name='cedula',
            field=models.CharField(max_length=50, null=True, verbose_name=b'No. C\xc3\xa9dula/DPI', blank=True),
        ),
        migrations.AlterField(
            model_name='respuestano41',
            name='agricola',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=7, null=True, choices=[(b'A', b'Falta de semilla'), (b'B', b'Mala calidad de la semilla'), (b'C', b'Falta de riego'), (b'D', b'Poca Tierra')]),
        ),
    ]
