# Generated by Django 2.2.16 on 2020-11-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0004_auto_20201126_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='build_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='作成日'),
        ),
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='目標日'),
        ),
    ]