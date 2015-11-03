from django.shortcuts import render
from django.http import HttpResponse
from matchmaker.forms import AddInstrumentForm, EditPersonalInfo
from matchmaker.models import Instrument, UserProfile
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)


@login_required
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


@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    user_instrument_list = Instrument.objects.filter(profile=request.user)
    context_dict = {'instruments': user_instrument_list, 'profile': user_profile}
    return render(request, 'profile.html', context_dict)

@login_required
def edit_personal_info(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        form = EditPersonalInfo(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return profile(request)
    else:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = UserProfile(user=request.user)
            user_profile.save()
        form = EditPersonalInfo(instance=user_profile)

    return render(request, 'edit_personal_info.html', {'form': form})
