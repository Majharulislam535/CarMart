# Generated by Django 5.0 on 2024-02-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand_model',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]