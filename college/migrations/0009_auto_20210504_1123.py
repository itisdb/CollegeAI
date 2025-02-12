# Generated by Django 3.1.4 on 2021-05-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_auto_20210316_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='college_type',
        ),
        migrations.AddField(
            model_name='college',
            name='about_us',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='meta_keywords',
            field=models.JSONField(blank=True, default=[], null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='meta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
