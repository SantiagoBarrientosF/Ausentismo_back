# Generated by Django 5.0.7 on 2024-09-18 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(default=' ', max_length=100)),
                ('Rol', models.CharField(max_length=100)),
                ('Sede', models.CharField(max_length=100)),
                ('Cargo', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='historial',
            name='fecha',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 117670, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 115128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 115128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 115128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 115128, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tiquetera',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_incorporacion',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_ingreso_empresa',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vacaciones',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 49, 46, 113069, tzinfo=datetime.timezone.utc)),
        ),
    ]
