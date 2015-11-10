from django.db import models
from django.contrib.auth.models import User

INSTRUMENT_CHOICES = (
    ("Electric Guitar", "Electric Guitar"),
    ("Acoustic Guitar", "Acoustic Guitar"),
    ("Accordion", "Accordion")
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
    ("Rock", "Rock"),
    ("Jazz", "Jazz")
)


class UserProfile(models.Model):
    """extends the built in User model"""
    user = models.OneToOneField(User, primary_key=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    location = models.CharField(max_length=50,choices=LOCATION_CHOICES, default="")
    bio = models.CharField(max_length=1000, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")


class Instrument(models.Model):
    profile = models.ForeignKey(User)
    years_of_experience = models.IntegerField()
    instrument_name = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)

class Genre(models.Model):
    genre_name = models.CharField(max_length=50, choices=GENRE_CHOICES)
    instrument = models.ManyToManyField(Instrument)

class Ensemble(models.Model):
    musicians = models.ManyToManyField(UserProfile)


