# Generated by Django 3.1.5 on 2021-07-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0030_auto_20210711_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegegenres',
            name='popular_course',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
