# Generated by Django 5.0.6 on 2024-10-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permisos',
            name='observaciones',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]