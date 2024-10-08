# Generated by Django 5.0.6 on 2024-10-03 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0056_rename_jefe_tiquetera_id_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiquetera',
            name='id_user',
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 871133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 871133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 871133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 871133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 871133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 870133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 870133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 869136, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 12, 49, 21, 869136, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 869136, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 866130, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 866130, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 12, 49, 21, 866130, tzinfo=datetime.timezone.utc)),
        ),
    ]
