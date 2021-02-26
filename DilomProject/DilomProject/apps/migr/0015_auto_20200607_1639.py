# Generated by Django 3.0.6 on 2020-06-07 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0014_position_area_system_area_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position_Areaa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_position', models.CharField(blank=True, max_length=30, verbose_name='System position')),
                ('system_area', models.CharField(blank=True, max_length=30, verbose_name='System area')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Position_Area',
        ),
    ]
