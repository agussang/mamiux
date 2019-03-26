# Generated by Django 2.1.7 on 2019-03-26 07:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0013_auto_20190323_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designcomment',
            name='design_abtest_comment',
            field=models.TextField(help_text='Kenapa kamu memilih pilihan itu? Bisa coba tolong jelaskan?', validators=[django.core.validators.MinLengthValidator(20, message='Minimal 20 karakter')], verbose_name='Komentar'),
        ),
    ]
