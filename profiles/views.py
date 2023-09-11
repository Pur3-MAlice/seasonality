from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Profile
from recipebook.models import Recipe


@login_required
def favourites(request):
    new = Recipe.newmanager.filter(favourites=request.user)
    return render(request, 'favourites.html', {'new': new})


@login_required
def favourite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            saved = True
            return render(request, 'profile.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                "saved": True
                })
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        saved = False

    recipes = Recipe.objects.all()
    new = Recipe.newmanager.filter(favourites=request.user)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        "saved": saved,
        "recipes": recipes,
        "new": new,
        })
