# Generated by Django 5.0.6 on 2024-10-03 13:05

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ausentismo', '0061_delete_beneficios_tiquetera_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='beneficios_tiquetera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficio', models.CharField(max_length=100)),
                ('horas_disponibles', models.CharField(max_length=80)),
                ('tipo', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_permiso', models.CharField(blank=True, null=True, unique=True)),
                ('cedula', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_ingreso_empresa', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 348078, tzinfo=datetime.timezone.utc))),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_peticion', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 348078, tzinfo=datetime.timezone.utc))),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 348078, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 348078, tzinfo=datetime.timezone.utc))),
                ('fecha_incorporacion', models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 13, 5, 40, 348078, tzinfo=datetime.timezone.utc))),
                ('jefe', models.CharField(max_length=80)),
                ('tipo_permiso', models.CharField(max_length=80)),
                ('parentesco', models.CharField(max_length=100, null=True)),
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
                ('fecha_ingreso_empresa', models.DateField(verbose_name=datetime.datetime(2024, 10, 3, 13, 5, 40, 344085, tzinfo=datetime.timezone.utc))),
                ('dias_vacaciones', models.CharField(max_length=5)),
                ('campaña', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 344085, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateField()),
                ('fecha_incorporacion', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 344085, tzinfo=datetime.timezone.utc))),
                ('observaciones', models.CharField(max_length=80)),
                ('jefe', models.CharField(max_length=80)),
                ('periodo', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Historial_permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_permiso', models.CharField(blank=True, null=True, unique=True)),
                ('cedula', models.CharField(max_length=30, null=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('correo', models.CharField(max_length=100, null=True)),
                ('fecha_ingreso_empresa', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 349081, tzinfo=datetime.timezone.utc))),
                ('campaña', models.CharField(max_length=100, null=True)),
                ('cargo', models.CharField(max_length=100, null=True)),
                ('fecha_peticion', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 349081, tzinfo=datetime.timezone.utc))),
                ('fecha_inicio', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 349081, tzinfo=datetime.timezone.utc))),
                ('fecha_fin', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 349081, tzinfo=datetime.timezone.utc))),
                ('fecha_incorporacion', models.DateField(default=datetime.datetime(2024, 10, 3, 13, 5, 40, 349081, tzinfo=datetime.timezone.utc))),
                ('jefe', models.CharField(max_length=80, null=True)),
                ('tipo_permiso', models.CharField(max_length=80, null=True)),
                ('parentesco', models.CharField(max_length=100, null=True)),
                ('id_permisos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ausentismo.permisos')),
            ],
        ),
        migrations.CreateModel(
            name='Tiquetera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=100)),
                ('codigo_tiquetera', models.CharField(blank=True, max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('campaña', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('beneficios', models.CharField(max_length=100, null=True)),
                ('correo', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100, null=True)),
                ('User_id', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]