# Generated by Django 5.0.6 on 2024-10-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ausentismo', '0008_rename_campaña_incapacidades_campana_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incapacidades',
            name='doc_incapacidad',
            field=models.FileField(blank=True, null=True, upload_to='incapacidades/'),
        ),
    ]
