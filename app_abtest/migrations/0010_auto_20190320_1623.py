# Generated by Django 2.1.7 on 2019-03-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0009_auto_20190320_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designcomment',
            name='design_abtest_tester_email',
            field=models.EmailField(blank=True, max_length=225, null=True, verbose_name='Email'),
        ),
    ]