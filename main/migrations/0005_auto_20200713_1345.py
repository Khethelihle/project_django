# Generated by Django 3.0.8 on 2020-07-13 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200713_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 13, 13, 45, 6, 780918), verbose_name='date published'),
        ),
    ]
