from django.urls import path
from django.http import HttpResponse


def error_view(request):
    """
    Simulate a server error
    :param request:
    :return:
    """
    raise Exception("Forced exception for testing 500 server error")


def fake_index_view(request):
    """
    Fake index view
    :param request:
    :return:
    """
    return HttpResponse("Fake Index")


urlpatterns = [
    path('', fake_index_view, name='index'),
    path('force-500/', error_view, name='force-500'),
]
