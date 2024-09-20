# Generated by Django 5.0.7 on 2024-09-18 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0017_alter_historial_fecha_alter_permisos_codigo_permisos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 893966, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='codigo_permisos',
            field=models.CharField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 892921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 892921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 892921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_fin',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 892921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 892921, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='Codigo_vacaciones',
            field=models.CharField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 891922, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 891922, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 24, 44, 891922, tzinfo=datetime.timezone.utc)),
        ),
    ]