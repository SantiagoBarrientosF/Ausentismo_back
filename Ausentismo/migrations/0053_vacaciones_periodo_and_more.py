# Generated by Django 5.0.6 on 2024-10-02 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0052_tiquetera_correo_tiquetera_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacaciones',
            name='periodo',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 660203, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 660203, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 660203, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 658117, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 654701, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 652056, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 2, 21, 9, 22, 654701, tzinfo=datetime.timezone.utc)),
        ),
    ]
