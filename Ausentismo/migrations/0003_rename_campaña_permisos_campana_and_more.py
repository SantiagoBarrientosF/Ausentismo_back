# Generated by Django 5.0.6 on 2024-10-16 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0002_permisos_observaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permisos',
            old_name='campaña',
            new_name='campana',
        ),
        migrations.RenameField(
            model_name='vacaciones',
            old_name='campaña',
            new_name='campana',
        ),
    ]
