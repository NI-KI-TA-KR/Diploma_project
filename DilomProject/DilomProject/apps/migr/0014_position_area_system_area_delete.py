# Generated by Django 3.0.6 on 2020-06-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_position_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='position_area',
            name='system_area_delete',
            field=models.CharField(blank=True, max_length=30, verbose_name='System area'),
        ),
    ]