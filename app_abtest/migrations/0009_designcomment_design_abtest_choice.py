# Generated by Django 2.1.7 on 2019-03-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0008_auto_20190312_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='designcomment',
            name='design_abtest_choice',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B')], max_length=1, null=True, verbose_name='A/B?'),
        ),
    ]
