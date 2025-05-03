import pytest
from django.urls import reverse


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


def test_simulate_error_view(client):
    """
    Test the simulate error view.
    :param client: The test client.
    """
    # Simulate a server error
    url = reverse('simulate-error')
    response = client.get(url)

    # Check that the response is 500 Internal Server Error
    assert response.status_code == 500

    # Check that the response contains the error message
    assert b"An error occurred" in response.content
