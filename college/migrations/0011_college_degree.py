# Generated by Django 3.1.4 on 2021-05-04 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_remove_college_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='degree',
            field=models.JSONField(null=True),
        ),
    ]
