# Generated by Django 3.1.4 on 2021-05-31 19:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_merge_20210504_1106'),
        ('college', '0015_auto_20210528_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedCollege',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'unique_together': {('college', 'profile')},
            },
        ),
    ]