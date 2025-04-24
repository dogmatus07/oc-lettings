from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Letting


def index(request):
    """
    View function for the letting index page.
    :param request:
    :return:
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function for a specific letting.
    :param request:
    :param letting_id:
    :return:
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)