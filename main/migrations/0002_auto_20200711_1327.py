# Generated by Django 3.0.8 on 2020-07-11 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 11, 13, 27, 40, 917898), verbose_name='date published'),
        ),
    ]