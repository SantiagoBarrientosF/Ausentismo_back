# Generated by Django 5.0.6 on 2024-09-24 14:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ausentismo', '0027_remove_historial_id_permisos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_permiso', models.CharField(blank=True, unique=True)),
                ('cedula', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_ingreso_empresa', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 372774, tzinfo=datetime.timezone.utc))),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_peticion', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 372774, tzinfo=datetime.timezone.utc))),
                ('fecha_incorporacion', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 372774, tzinfo=datetime.timezone.utc))),
                ('observaciones', models.CharField(max_length=80)),
                ('jefe', models.CharField(max_length=80)),
                ('tipo_permiso', models.CharField(max_length=80)),
                ('parentesco', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tiquetera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('campaña', models.CharField(max_length=100)),
                ('jefe', models.CharField(max_length=100)),
                ('fecha_peticion', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('beneficios', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
                ('tipo_tiquetera', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_vacacione', models.CharField(blank=True, unique=True)),
                ('cedula', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_ingreso_empresa', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 370570, tzinfo=datetime.timezone.utc))),
                ('dias_vacaciones', models.CharField(max_length=5)),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 371125, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateField()),
                ('fecha_incorporacion', models.DateField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 371125, tzinfo=datetime.timezone.utc))),
                ('observaciones', models.CharField(max_length=80)),
                ('jefe', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 24, 14, 7, 14, 373311, tzinfo=datetime.timezone.utc))),
                ('id_permisos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ausentismo.permisos')),
                ('id_tiquetera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ausentismo.tiquetera')),
                ('id_vacaciones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ausentismo.vacaciones')),
            ],
        ),
    ]
