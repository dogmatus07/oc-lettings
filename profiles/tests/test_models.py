import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_str():
    """
    Test the __str__ method of the Profile model.

    Args:
        None

    Returns:
        None
    """
    user = User.objects.create(username='usertester')
    profile = Profile.objects.create(user=user, favorite_city='Los Angeles')
    assert str(profile) == 'usertester'
    assert str(profile.favorite_city) == 'Los Angeles'
