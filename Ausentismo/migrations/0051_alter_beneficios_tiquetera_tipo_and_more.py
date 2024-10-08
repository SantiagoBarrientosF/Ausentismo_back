# Generated by Django 5.0.6 on 2024-10-02 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0050_remove_tiquetera_tipo_tiquetera_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficios_tiquetera',
            name='tipo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 20, 6, 29, 142815, tzinfo=datetime.timezone.utc)),
        ),
    ]
