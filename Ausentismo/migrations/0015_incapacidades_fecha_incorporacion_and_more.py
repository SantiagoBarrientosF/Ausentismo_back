# Generated by Django 5.0.6 on 2024-10-21 16:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0014_tiquetera_observaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='incapacidades',
            name='fecha_incorporacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='incapacidades',
            name='fecha_inicio',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='incapacidades',
            name='radicado',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
