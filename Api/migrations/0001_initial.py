# Generated by Django 4.2.3 on 2023-11-13 18:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('release_year', models.IntegerField()),
                ('rating', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])),
                ('geners', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), size=None)),
                ('actors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), size=None)),
            ],
        ),
    ]
