# Generated by Django 3.1.5 on 2021-07-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0023_collegegenres_url_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegegenres',
            name='url_tag',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
