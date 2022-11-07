# Generated by Django 4.0.8 on 2022-11-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_slug_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=55, unique=True, verbose_name='Slug'),
        ),
    ]
