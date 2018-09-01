# Generated by Django 2.0.6 on 2018-08-05 21:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Securities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('market', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Strategies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security', models.CharField(max_length=50)),
                ('strategy', django.contrib.postgres.fields.jsonb.JSONField()),
                ('percentage_up', models.FloatField(default=None)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('max_point', models.FloatField(null=True)),
                ('min_point', models.FloatField(null=True)),
            ],
        ),
    ]