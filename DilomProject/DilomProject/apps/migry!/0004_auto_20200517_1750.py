# Generated by Django 3.0.6 on 2020-05-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200517_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume_github',
            field=models.URLField(max_length=30, verbose_name='Github link'),
        ),
    ]
