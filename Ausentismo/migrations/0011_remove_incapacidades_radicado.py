# Generated by Django 5.0.6 on 2024-10-17 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0010_incapacidades_lider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incapacidades',
            name='radicado',
        ),
    ]
