# Generated by Django 4.0.8 on 2022-11-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0004_alter_bot_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='poster',
            field=models.ImageField(blank=True, default='', upload_to='posters/', verbose_name='Poster'),
        ),
    ]
