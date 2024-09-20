# Generated by Django 5.0.7 on 2024-09-18 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacaciones',
            name='fecha_fin',
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 107475, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 105569, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 97512, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 14, 12, 105569, tzinfo=datetime.timezone.utc)),
        ),
    ]