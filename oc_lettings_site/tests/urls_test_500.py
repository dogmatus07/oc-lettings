from django.urls import path
from django.http import HttpResponse


def error_view(request):
    """
    Simulate a server error

    Args:
        request: The HTTP request object.

    Returns:
        None

    Raises:
        Exception: Always raises an exception to simulate a 500 server error.
    """
    raise Exception("Forced exception for testing 500 server error")


def fake_index_view(request):
    """
    Fake index view

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A simple HTTP response indicating the index page.
    """
    return HttpResponse("Fake Index")


urlpatterns = [
    path('', fake_index_view, name='index'),
    path('force-500/', error_view, name='force-500'),
]
