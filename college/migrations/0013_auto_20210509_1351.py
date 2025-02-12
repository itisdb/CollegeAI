# Generated by Django 3.1.4 on 2021-05-09 13:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0012_auto_20210505_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeFacilities',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('icon', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='college',
            name='facilities',
            field=models.ManyToManyField(to='college.CollegeFacilities'),
        ),
    ]
