# Generated by Django 2.1.7 on 2019-03-11 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0002_auto_20190309_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='design_password',
        ),
    ]
