from django.shortcuts import render
from django.http import HttpResponse
from matchmaker.forms import AddInstrumentForm


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'index.html', context_dict)


def add_instrument(request):
    if request.method == 'POST':
        form = AddInstrumentForm(request.POST)
        if form.is_valid():
            # Save the new category to the database.
            instrument_form = form.save(commit=False)
            instrument_form.profile = request.user
            instrument_form.save()

            # The user will be shown the homepage.
            return index(request)
    else:
        form = AddInstrumentForm()

    return render(request, 'add_instrument.html', {'form': form})

