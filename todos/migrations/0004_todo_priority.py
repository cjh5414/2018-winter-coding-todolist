# Generated by Django 2.1.2 on 2018-11-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20181103_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=-1),
        ),
    ]
