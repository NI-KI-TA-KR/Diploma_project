# Generated by Django 3.0.6 on 2020-05-18 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20200517_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='resume',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]