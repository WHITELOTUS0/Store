# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-24 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Company Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'company_logo/', verbose_name='Logo')),
                ('slogan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Slogan')),
                ('short_description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Description')),
                ('long_description', models.CharField(blank=True, max_length=800, null=True, verbose_name='Long Description')),
                ('Mission', models.CharField(blank=True, max_length=800, null=True, verbose_name='Mission')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'location_logo/', verbose_name='photo')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Description')),
                ('Mission', models.CharField(blank=True, max_length=800, null=True, verbose_name='Mission')),
                ('createdAt', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, verbose_name='Location Type')),
            ],
            options={
                'verbose_name': 'Location Type',
                'verbose_name_plural': 'Location Types',
            },
        ),
        migrations.AddField(
            model_name='location',
            name='fk_locationType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.LocationType', verbose_name='Location Type'),
        ),
    ]
