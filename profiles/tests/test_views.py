import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_view(client):
    """
    Test the profile index view.
    :param client: The test client.
    """
    # Create a test profile
    user = User.objects.create(username='usertester')
    Profile.objects.create(user=user, favorite_city='Los Angeles')

    # Get the response from the index view
    url = reverse('profiles:index')
    response = client.get(url)

    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the profile is in the context
    assert b"usertester" in response.content


@pytest.mark.django_db
def test_profile_detail_view(client):
    """
    Test the profile detail view.
    :param client: The test client.
    """
    # Create a test profile for the detail view
    user = User.objects.create(username='usertester')
    Profile.objects.create(user=user, favorite_city='Los Angeles')

    # Get the response from the profile detail view
    url = reverse('profiles:profile', args=[user.username])
    response = client.get(url)

    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the profile details are in the context
    assert b"usertester" in response.content
    assert b"Los Angeles" in response.content
