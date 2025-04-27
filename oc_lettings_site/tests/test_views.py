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
