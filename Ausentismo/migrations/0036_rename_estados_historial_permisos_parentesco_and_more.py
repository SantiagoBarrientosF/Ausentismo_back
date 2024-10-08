# Generated by Django 5.0.6 on 2024-10-01 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0035_alter_historial_permisos_fecha_fin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historial_permisos',
            old_name='Estados',
            new_name='parentesco',
        ),
        migrations.AddField(
            model_name='historial_permisos',
            name='codigo_permiso',
            field=models.CharField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='historial_permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 133450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 133450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 133450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 133450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 133450, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 132942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 132942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 132942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 1, 20, 29, 7, 132942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 132942, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 130939, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 130939, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 1, 20, 29, 7, 130939, tzinfo=datetime.timezone.utc)),
        ),
    ]
