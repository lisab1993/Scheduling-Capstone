# Generated by Django 3.1.6 on 2021-03-04 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistapp', '0006_auto_20210304_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 10, 55, 33, 273222)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 10, 55, 33, 272222)),
        ),
        migrations.AlterField(
            model_name='eventtask',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 10, 55, 33, 273222)),
        ),
    ]
