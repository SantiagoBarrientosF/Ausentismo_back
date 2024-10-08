# Generated by Django 5.0.6 on 2024-10-03 19:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0062_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='jefe',
        ),
        migrations.RemoveField(
            model_name='vacaciones',
            name='jefe',
        ),
        migrations.AddField(
            model_name='permisos',
            name='User_id',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vacaciones',
            name='User_id',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='historial_permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_peticion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2024, 10, 3, 19, 36, 18, 952884, tzinfo=datetime.timezone.utc)),
        ),
    ]
