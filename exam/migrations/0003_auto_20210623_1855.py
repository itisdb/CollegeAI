# Generated by Django 3.1.5 on 2021-06-23 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210623_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='application_form',
            new_name='exam_pattern',
        ),
        migrations.RemoveField(
            model_name='examgenres',
            name='icon',
        ),
    ]