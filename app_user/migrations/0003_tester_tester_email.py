# Generated by Django 2.1.7 on 2019-03-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_auto_20190314_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='tester',
            name='tester_email',
            field=models.EmailField(blank=True, max_length=225, null=True, verbose_name='Tester Email'),
        ),
    ]