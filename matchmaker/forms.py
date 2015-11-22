from django import forms
from matchmaker.models import Instrument, UserProfile, Genre, INSTRUMENT_CHOICES, LOCATION_CHOICES, GENDER_CHOICES, GENRE_CHOICES


class AddInstrumentForm(forms.ModelForm):
    instrument_name = forms.ChoiceField(choices=INSTRUMENT_CHOICES,)
    years_of_experience = forms.IntegerField(initial=0, min_value=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Instrument
        fields = ('instrument_name', 'years_of_experience')

class AddGenres(forms.ModelForm):
    genre_name = forms.ChoiceField(choices=GENRE_CHOICES)
    class Meta:
        model = Genre
        fields = ['genre_name']

class EditPersonalInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'location', 'bio']
