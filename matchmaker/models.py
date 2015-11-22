from django.db import models
from django.contrib.auth.models import User

INSTRUMENT_CHOICES = (
    ("Accordion", "Accordion"),
    ("Bagpipes", "Bagpipes"),
    ("Banjo", "Banjo"),
    ("Bassoon", "Bassoon"),
    ("Bongo Drums", "Bongo Drums"),
    ("Bugle", "Bugle"),
    ("Clarinet", "Clarinet"),
    ("Clarinet - Baritone", "Clarinet - Baritone"),
    ("Clarinet - Soprano", "Clarinet - Soprano"),
    ("Digeridoo", "Digeridoo"),
    ("Double Bass", "Double Bass"),
    ("Drum Set", "Drum Set"),
    ("Fiddle", "Fiddle"),
    ("Flute", "Flute"),
    ("French Horn", "French Horn"),
    ("Guitar - Electric", "Guitar - Electric"),
    ("Guitar - Accoustic", "Guitar - Accoustic"),
    ("Guitar - Bass", "Guitar - Bass"),
    ("Harmonica", "Harmonica"),
    ("Harp", "Harp"),
    ("Keyboard", "Keyboard"),
    ("Mandolin", "Mandolin"),
    ("Oboe", "Oboe"),
    ("Organ", "Pipe Organ"),
    ("Piano", "Piano"),
    ("Piccolo", "Piccolo"),
    ("Saxophone - Alto", "Saxophone - Alto"),
    ("Saxophone - Baritone", "Saxophone - Baritone"),
    ("Saxophone - Tenor", "Saxophone - Tenor"),
    ("Sitar", "Sitar"),
    ("Tamborine", "Tamborine"),
    ("Trombone", "Trombone"),
    ("Trumpet", "Trumpet"),
    ("Tuba", "Tuba"),
    ("Ukulele", "Ukulele"),
    ("Viola", "Viola"),
    ("Violin", "Violin"),
    ("Xylophone", "Xylophone")
)

LOCATION_CHOICES = (
    ("Vancouver","Vancouver"),
    ("Victoria","Victoria")
)

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)

GENRE_CHOICES = (
    ("Alternative Rock", "Alternative Rock"),
    ("Black/Death Metal", "Black/Death Metal"),
    ("Blues", "Blues"),
    ("Bluegrass", "Bluegrass"),
    ("Classical", "Classical"),
    ("Country", "Country"),
    ("Dance", "Dance"),
    ("Dubstep", "Dubstep"),
    ("Electronic", "Electronic"),
    ("Folk", "Folk"),
    ("Funk", "Funk"),
    ("Gospel", "Gospel"),
    ("Grunge", "Grunge"),
    ("Hard Rock", "Hard Rock"),
    ("Hip-Hop", "Hip-Hop"),
    ("Indie Rock", "Indie Rock"),
    ("Jazz", "Jazz"),
    ("K-Pop", "K-Pop"),
    ("Latin", "Latin"),
    ("Metal", "Metal"),
    ("Musical Theater", "Musical Theater"),
    ("Opera", "Opera"),
    ("Punk", "Punk"),
    ("Rap", "Rap"),
    ("Reggae", "Reggae"),
    ("RB/Soul", "RB/Soul"),
    ("Rock", "Rock"),
    ("Soft Rock", "Soft Rock")
)


class UserProfile(models.Model):
    """extends the built in User model"""
    user = models.OneToOneField(User, primary_key=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    birth_date = models.DateField(null=True)
    location = models.CharField(max_length=50,choices=LOCATION_CHOICES, default="")
    bio = models.CharField(max_length=1000, default="")


class Instrument(models.Model):
    profile = models.ForeignKey(User)
    instrument_name = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)
    years_of_experience = models.IntegerField()

class Genre(models.Model):
    profile = models.ForeignKey(User)
    genre_name = models.CharField(max_length=50, choices=GENRE_CHOICES)

class Ensemble(models.Model):
    musicians = models.ManyToManyField(UserProfile)


