# Generated by Django 4.1.1 on 2022-09-24 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ads_cars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='cars',
            new_name='car',
        ),
    ]