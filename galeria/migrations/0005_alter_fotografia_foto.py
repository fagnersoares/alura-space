# Generated by Django 5.0.6 on 2024-06-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0004_fotografia_data_fotografica"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]