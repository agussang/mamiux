# Generated by Django 2.1.7 on 2019-03-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abtest', '0012_auto_20190323_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designcomment',
            name='design_abtest_choice',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B')], help_text='Mana yang menurut kamu paling mudah digunakan? A atau B?', max_length=1, null=True, verbose_name='Pilih A/B?'),
        ),
        migrations.AlterField(
            model_name='designcomment',
            name='design_abtest_comment',
            field=models.TextField(help_text='Kenapa kamu memilih pilihan itu? Bisa coba jelaskan?', verbose_name='Komentar'),
        ),
    ]
