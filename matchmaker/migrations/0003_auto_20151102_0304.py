# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0002_auto_20151029_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='', max_length=50, choices=[('Vancouver', 'Vancouver'), ('Victoria', 'Victoria')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='', max_length=1),
        ),
    ]
