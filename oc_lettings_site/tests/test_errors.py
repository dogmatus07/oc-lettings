import types
import pytest
from django.urls import reverse
from django.http import HttpResponseServerError
from django.urls import path, clear_url_caches, set_urlconf


@pytest.mark.django_db
def test_custom_404_view(client):
    """
    Test the custom 404 error page
    :param client: test client
    """
    response = client.get('/not-a-page/')
    assert response.status_code == 404
    assert b'Page not found' in response.content


@pytest.mark.django_db
def test_custom_500_view(client):
    """
    Test the custom 500 error page
    :param client: test client
    """
    def error_view(request):
        raise Exception("Test exception")

    test_urls = types.ModuleType("test_urls")
    test_urls.urlpatterns = [
        path('force-500/', error_view)
    ]

    clear_url_caches()
    set_urlconf(test_urls)
    response = client.get('/force-500/', follow=False, raise_request_exception=False)
    assert response.status_code == 500
    assert b'Server Error' in response.content

