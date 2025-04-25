from django.shortcuts import render
from lettings.models import Letting
from profiles.models import Profile


def index(request):
    """
    View function for the index page.
    :param request:
    :return: index.html
    """
    return render(request, 'index.html')
