from django.shortcuts import render
from django.http import HttpResponse
from matchmaker.forms import AddInstrumentForm, EditPersonalInfo, AddGenres
from matchmaker.models import Instrument, UserProfile, Genre
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
            return (request)
    else:
        form = AddInstrumentForm()

    return render(request, 'add_instrument.html', {'form': form})


@login_required
def add_genre(request):
    if request.method == 'POST':
        form = AddGenres(request.POST)
        if form.is_valid():
            # Save the new category to the database.
            genre_form = form.save(commit=False)
            genre_form.profile = request.user
            genre_form.save()

            # The user will be shown the homepage.
            return profile(request)
    else:
        form = AddGenres()

    return render(request, 'add_genre.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()
    user_genre_list = Genre.objects.filter(profile=request.user)
    user_instrument_list = Instrument.objects.filter(profile=request.user)
    context_dict = {'instruments': user_instrument_list, 'genres': user_genre_list, 'profile': user_profile}
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

@login_required
def matches(request):
    users_in_area = UserProfile.objects.filter(location=request.user.userprofile.location).exclude(user=request.user)
    genres_in_common = {}
    request_user_genres_query_set = Genre.objects.filter(profile=request.user)
    request_user_genres_set = {x.genre_name for x in request_user_genres_query_set}

    for user_profile in users_in_area:
        user_profile_genres_query_set = Genre.objects.filter(profile=user_profile.user)
        user_profile_genres_set = {x.genre_name for x in user_profile_genres_query_set}
        intersect_number = len(user_profile_genres_set & request_user_genres_set)
        genres_in_common[user_profile] = intersect_number

    users_tuples = genres_in_common.items()
    sorted_users = sorted(users_tuples,key=lambda x: x[1],reverse=True)
    final_list = [x[0] for x in sorted_users]

    context_dict = {'matches': final_list}
    return render(request, 'matches.html', context_dict)
