# Generated by Django 2.2.16 on 2020-12-26 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0008_auto_20201226_2116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudyDetail',
            new_name='StudySet',
        ),
        migrations.AlterField(
            model_name='project',
            name='build_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 26, 21, 50, 5, 291464), verbose_name='作成日'),
        ),
    ]