# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring', '0012_auto_20170819_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='wage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
