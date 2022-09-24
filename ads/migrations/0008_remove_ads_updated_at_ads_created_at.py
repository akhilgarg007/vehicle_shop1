# Generated by Django 4.1.1 on 2022-09-24 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_rename_cars_ads_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='ads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
