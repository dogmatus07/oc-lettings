import pytest
from django.urls import reverse
from oc_lettings_site.views import index


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
    assert 'lettings' in response.context
    assert 'profiles' in response.context
