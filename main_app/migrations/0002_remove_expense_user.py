# Generated by Django 4.1.2 on 2022-10-19 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
