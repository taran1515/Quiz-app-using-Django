# Generated by Django 3.0.6 on 2020-05-27 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='User',
        ),
    ]
