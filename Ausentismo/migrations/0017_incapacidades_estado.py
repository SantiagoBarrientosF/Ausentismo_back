# Generated by Django 5.0.6 on 2024-10-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0016_incapacidades_fecha_peticion'),
    ]

    operations = [
        migrations.AddField(
            model_name='incapacidades',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=100),
        ),
    ]
