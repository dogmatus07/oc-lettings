import pytest
from django.test import override_settings, RequestFactory
from django.views import defaults


@pytest.mark.django_db
def test_custom_404_view(client):
    """
    Test the custom 404 error page

    Args:
        client: The test client to simulate requests.

    Returns:
        None
    """
    response = client.get('not-a-page/')
    assert response.status_code == 404
    assert b'Page not found' in response.content


@pytest.mark.django_db
@override_settings(
    DEBUG=False,
    ROOT_URLCONF='oc_lettings_site.tests.urls_test_500',
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['oc_lettings_site/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
)
def test_custom_500_view():
    """
    Test the custom 500 error page, simulate an exception
    Call the default Django 500 error view

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the response status code is not 500 or \n
        if the content does not contain 'Server Error'.
    """

    factory = RequestFactory()
    request = factory.get('/force-500/')
    response = None

    try:
        from oc_lettings_site.tests.urls_test_500 import error_view
        error_view(request)
    except Exception:
        response = defaults.server_error(request, template_name='500.html')

    assert response.status_code == 500
    assert b'Server Error' in response.content
