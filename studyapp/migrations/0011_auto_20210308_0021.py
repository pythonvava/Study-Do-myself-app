# Generated by Django 2.2.16 on 2021-03-07 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0010_auto_20210214_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setplan',
            name='count',
        ),
        migrations.RemoveField(
            model_name='setplan',
            name='sumtime',
        ),
        migrations.AddField(
            model_name='setplan',
            name='sets',
            field=models.IntegerField(choices=[('', 'sets'), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default=None, verbose_name='セット回数'),
        ),
        migrations.AddField(
            model_name='setplan',
            name='total',
            field=models.IntegerField(default=1, verbose_name='総勉強時間'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='build_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 8, 0, 20, 1, 63726), verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='setplan',
            name='minute',
            field=models.IntegerField(choices=[('', 'minute'), ('1', 15), ('2', 25), ('3', 50)], default=None, verbose_name='分'),
        ),
    ]
