# Generated by Django 2.1.2 on 2018-11-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
