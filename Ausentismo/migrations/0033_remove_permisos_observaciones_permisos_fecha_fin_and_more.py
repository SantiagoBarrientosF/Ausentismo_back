# Generated by Django 5.0.6 on 2024-09-27 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0032_tiquetera_codigo_tiquetera_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='observaciones',
        ),
        migrations.AddField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 325163, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 313113, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 313113, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 27, 16, 57, 44, 313113, tzinfo=datetime.timezone.utc)),
        ),
    ]
