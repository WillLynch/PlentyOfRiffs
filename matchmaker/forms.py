from django import forms
from matchmaker.models import Instrument, UserProfile, INSTRUMENT_CHOICES, LOCATION_CHOICES, GENDER_CHOICES


class AddInstrumentForm(forms.ModelForm):
    instrument_name = forms.ChoiceField(choices=INSTRUMENT_CHOICES,)
    years_of_experience = forms.IntegerField(initial=0, min_value=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Instrument
        fields = ('instrument_name', 'years_of_experience')


class EditPersonalInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'gender', 'location', 'bio', 'first_name', 'last_name']
