# Generated by Django 3.1.5 on 2021-06-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210625_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meta_keywords',
            field=models.JSONField(blank=True, default={}, null=True),
        ),
    ]
