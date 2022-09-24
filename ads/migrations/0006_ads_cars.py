# Generated by Django 4.1.1 on 2022-09-24 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('ads', '0005_alter_ads_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='cars',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.car'),
            preserve_default=False,
        ),
    ]