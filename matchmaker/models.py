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
    ("Male", "M"),
    ("Female", "F"),
    ("Other", "O")
)


class UserProfile(models.Model):
    """extends the built in User model"""
    user = models.OneToOneField(User, primary_key=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, default="")
    location = models.CharField(max_length=50,choices=LOCATION_CHOICES, default="")
    bio = models.CharField(max_length=1000, default="")


class Instrument(models.Model):
    profile = models.ForeignKey(User)
    years_of_experience = models.IntegerField()
    instrument_name = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)


class Ensemble(models.Model):
    musicians = models.ManyToManyField(UserProfile)


