# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-17 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='Coding Dojo studio'),
            preserve_default=False,
        ),
    ]