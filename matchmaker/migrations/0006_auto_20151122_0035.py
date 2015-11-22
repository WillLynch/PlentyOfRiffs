# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matchmaker', '0005_auto_20151103_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_name', models.CharField(max_length=50, choices=[('Alternative Rock', 'Alternative Rock'), ('Black/Death Metal', 'Black/Death Metal'), ('Blues', 'Blues'), ('Bluegrass', 'Bluegrass'), ('Classical', 'Classical'), ('Country', 'Country'), ('Dance', 'Dance'), ('Dubstep', 'Dubstep'), ('Electronic', 'Electronic'), ('Folk', 'Folk'), ('Funk', 'Funk'), ('Gospel', 'Gospel'), ('Grunge', 'Grunge'), ('Hard Rock', 'Hard Rock'), ('Hip-Hop', 'Hip-Hop'), ('Indie Rock', 'Indie Rock'), ('Jazz', 'Jazz'), ('K-Pop', 'K-Pop'), ('Latin', 'Latin'), ('Metal', 'Metal'), ('Musical Theater', 'Musical Theater'), ('Opera', 'Opera'), ('Punk', 'Punk'), ('Rap', 'Rap'), ('Reggae', 'Reggae'), ('RB/Soul', 'RB/Soul'), ('Rock', 'Rock'), ('Soft Rock', 'Soft Rock')])),
                ('profile', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='instrument',
            name='instrument_name',
            field=models.CharField(max_length=50, choices=[('Accordion', 'Accordion'), ('Bagpipes', 'Bagpipes'), ('Banjo', 'Banjo'), ('Bassoon', 'Bassoon'), ('Bongo Drums', 'Bongo Drums'), ('Bugle', 'Bugle'), ('Clarinet', 'Clarinet'), ('Clarinet - Baritone', 'Clarinet - Baritone'), ('Clarinet - Soprano', 'Clarinet - Soprano'), ('Digeridoo', 'Digeridoo'), ('Double Bass', 'Double Bass'), ('Drum Set', 'Drum Set'), ('Fiddle', 'Fiddle'), ('Flute', 'Flute'), ('French Horn', 'French Horn'), ('Guitar - Electric', 'Guitar - Electric'), ('Guitar - Accoustic', 'Guitar - Accoustic'), ('Guitar - Bass', 'Guitar - Bass'), ('Harmonica', 'Harmonica'), ('Harp', 'Harp'), ('Keyboard', 'Keyboard'), ('Mandolin', 'Mandolin'), ('Oboe', 'Oboe'), ('Organ', 'Pipe Organ'), ('Piano', 'Piano'), ('Piccolo', 'Piccolo'), ('Saxophone - Alto', 'Saxophone - Alto'), ('Saxophone - Baritone', 'Saxophone - Baritone'), ('Saxophone - Tenor', 'Saxophone - Tenor'), ('Sitar', 'Sitar'), ('Tamborine', 'Tamborine'), ('Trombone', 'Trombone'), ('Trumpet', 'Trumpet'), ('Tuba', 'Tuba'), ('Ukulele', 'Ukulele'), ('Viola', 'Viola'), ('Violin', 'Violin'), ('Xylophone', 'Xylophone')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')]),
        ),
    ]
