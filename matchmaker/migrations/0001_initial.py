# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ensemble',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('years_of_experience', models.IntegerField()),
                ('instrument_name', models.CharField(choices=[('Electric Guitar', 'Electric Guitar'), ('Acoustic Guitar', 'Acoustic Guitar'), ('Accordion', 'Accordion')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='profile',
            field=models.ForeignKey(to='matchmaker.UserProfile'),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='musicians',
            field=models.ManyToManyField(to='matchmaker.UserProfile'),
        ),
    ]
