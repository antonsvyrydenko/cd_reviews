# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-08 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
