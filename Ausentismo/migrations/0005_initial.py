# Generated by Django 5.0.7 on 2024-09-18 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ausentismo', '0004_remove_historial_id_proceso_delete_permisos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 515250, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_ingreso_empresa', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 515250, tzinfo=datetime.timezone.utc))),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 515250, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 515250, tzinfo=datetime.timezone.utc))),
                ('fecha_incorporacion', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 515250, tzinfo=datetime.timezone.utc))),
                ('observaciones', models.CharField(max_length=80)),
                ('jefe', models.CharField(max_length=80)),
                ('tipo_permiso', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Tiquetera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 514742, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 514742, tzinfo=datetime.timezone.utc))),
                ('tipo_tiquetera', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_ingreso_empresa', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 512805, tzinfo=datetime.timezone.utc))),
                ('dias_vacaciones', models.CharField(max_length=5)),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 512805, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 512805, tzinfo=datetime.timezone.utc))),
                ('fecha_incorporacion', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 18, 13, 46, 40, 512805, tzinfo=datetime.timezone.utc))),
                ('observaciones', models.CharField(max_length=80)),
                ('jefe', models.CharField(max_length=80)),
            ],
        ),
    ]
