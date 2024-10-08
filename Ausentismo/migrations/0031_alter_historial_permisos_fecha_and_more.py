# Generated by Django 5.0.6 on 2024-09-26 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0030_alter_historial_permisos_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 9, 26, 17, 9, 57, 772913, tzinfo=datetime.timezone.utc)),
        ),
    ]
