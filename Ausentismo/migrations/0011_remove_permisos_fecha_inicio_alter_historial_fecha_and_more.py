# Generated by Django 5.0.7 on 2024-09-18 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0010_remove_vacaciones_fecha_fin_alter_historial_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='fecha_inicio',
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 664298, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 662923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 662923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 662923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 662923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 662923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 661670, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 661670, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 20, 19, 42, 661670, tzinfo=datetime.timezone.utc)),
        ),
    ]