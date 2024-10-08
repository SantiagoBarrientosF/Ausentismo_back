# Generated by Django 5.0.7 on 2024-09-18 21:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0022_alter_historial_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='codigo_permiso',
        ),
        migrations.RemoveField(
            model_name='vacaciones',
            name='Codigo_vacacione',
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 674256, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 673257, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 673257, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 673257, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_fin',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 672259, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 672259, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 671275, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 671275, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 18, 21, 27, 48, 671275, tzinfo=datetime.timezone.utc)),
        ),
    ]
