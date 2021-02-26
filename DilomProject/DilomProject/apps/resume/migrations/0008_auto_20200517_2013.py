# Generated by Django 3.0.6 on 2020-05-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='resume_birthday',
        ),
        migrations.AddField(
            model_name='resume',
            name='resume_years',
            field=models.CharField(default='0', max_length=3, verbose_name='Years'),
            preserve_default=False,
        ),
    ]
