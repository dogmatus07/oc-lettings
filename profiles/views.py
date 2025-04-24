from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """
    View function for the profiles index page.
    :param request:
    :return:
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function for a specific profile.
    :param request:
    :param username:
    :return:
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        'profile': profile,
        'favorite_city': profile.favorite_city,
    }
    return render(request, 'profiles/profile.html', context)
