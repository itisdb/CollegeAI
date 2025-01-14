# Generated by Django 3.1.5 on 2021-03-23 11:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201227_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='psychometry',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('infrastructure', models.IntegerField()),
                ('academics', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
