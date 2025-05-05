import pytest
from unittest import mock
from django.test import RequestFactory
from django.http import HttpResponse
from django.urls import reverse

from oc_lettings_site.views import custom_404_view, custom_500_view


@pytest.mark.django_db
def test_index_view(client):
    """
    Test the main index view.
    :param client: The test client.
    """
    # Get the response from the index view
    url = reverse('index')
    response = client.get(url)

    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the index template is used
    assert 'index.html' in [t.name for t in response.templates]

    # Check that the context contains the expected data
    assert b'lettings' in response.content
    assert b'profiles' in response.content


@pytest.mark.django_db
@mock.patch('oc_lettings_site.views.render')
def test_index_view_exception(mock_render, client):
    """
    Force Exception on index view
    :param mock_render: mock render
    :param client: test client
    """
    mock_render.side_effect = Exception("Render failed")
    response = client.get(reverse('index'))
    assert response.status_code == 500
    assert b"An error occurred while rendering the index page." in response.content


def test_custom_404_view_render_success():
    """
    Render success for custom 404 view
    """
    factory = RequestFactory()
    request = factory.get('not-found-page')

    with mock.patch('oc_lettings_site.views.render') as mock_render:
        mock_render.return_value.status_code = 404
        response = custom_404_view(request, exception=None)

    assert response.status_code == 404


def test_custom_404_view_render_exception():
    """
    Render Exception for custom 404 view
    """
    factory = RequestFactory()
    request = factory.get('not-found-page')

    with mock.patch('oc_lettings_site.views.render', side_effect=Exception('Rendering Failed')):
        response = custom_404_view(request, exception=None)

    assert response.status_code == 500
    assert b"An error occurred while rendering the 404 page" in response.content


def test_custom_500_view_render_success():
    """
    Test render success for custom 500 view
    :return:
    """
    factory = RequestFactory()
    request = factory.get('/server-error/')

    with mock.patch('oc_lettings_site.views.render') as mock_render:
        mock_render.return_value.status_code = 500
        response = custom_500_view(request)

    assert response.status_code == 500


def test_custom_500_view_render_exception():
    """
    Test render exception for custom 500 view
    """
    factory = RequestFactory()
    request = factory.get('/server-error/')

    with mock.patch('oc_lettings_site.views.render', side_effect=Exception('Rendering Failed')):
        response = custom_500_view(request)

    assert response.status_code == 500
    assert b"An error occurred while rendering the 500 page" in response.content


def test_custom_404_view(client):
    """
    Test the custom 404 error view.
    :param client: The test client.
    """
    # Get the response from a non-existent page
    url = reverse('index') + 'not-a-page/'
    response = client.get(url)

    # Check that the response is 404 Not Found
    assert response.status_code == 404

    # Check that the 404 template is used
    assert '404.html' in [t.name for t in response.templates]


def test_custom_500_view(client):
    """
    Test the custom 500 error view.
    :param client: The test client.
    """
    # Simulate a server error
    url = reverse('simulate-error')
    response = client.get(url)

    # Check that the response is 500 Internal Server Error
    assert response.status_code == 500

@pytest.mark.django_db
def test_simulate_error_view(client):
    """
    Test the simulate error view.
    :param client: The test client.
    """

    with mock.patch('oc_lettings_site.views.logger') as mock_logger, \
        mock.patch('oc_lettings_site.views.sentry_sdk.capture_exception') as mock_sentry:

        # Simulate a server error
        url = reverse('simulate-error')
        response = client.get(url)

        # Check that a HttpResponse instance is returned
        assert isinstance(response, HttpResponse)
        assert b"An error occurred, and it has been logged." in response.content

        # Check that the response is 500 Internal Server Error
        assert response.status_code == 500

        # Check that the response contains the error message
        assert b"An error occurred" in response.content

        # Check that logger and sentry have been called properly
        assert mock_logger.error.called
        assert mock_sentry.called
