# Generated by Django 3.0.6 on 2020-05-27 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mvr', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(default=datetime.datetime.now)),
                ('birth_date', models.DateTimeField()),
            ],
        ),
    ]