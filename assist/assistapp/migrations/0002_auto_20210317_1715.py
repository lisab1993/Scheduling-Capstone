# Generated by Django 3.1.6 on 2021-03-18 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtask',
            name='priority',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
    ]
