# Generated by Django 3.1.6 on 2021-03-02 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtask',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='eventtask',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_tasks', to='assistapp.priority'),
        ),
    ]