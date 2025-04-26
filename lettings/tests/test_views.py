import pytest
from django.urls import reverse
from lettings.models import Letting, Address

@pytest.mark.django_db
def test_lettings_index_view(client):
    """
    Test the lettings index view.
    :param client: The test client.
    """
    # Create a sample letting
    # create a fake address
    fake_address = Address.objects.create(
        number=123,
        street='Test street',
        city='Los Angeles',
        state='CA',
        zip_code='90001'
    )
    letting = Letting.objects.create(
        title='My Letting',
        address=fake_address,
    )

    # Get the response from the index view
    url = reverse('lettings:index')
    response = client.get(url)

    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the letting is in the context
    assert b"My Letting" in response.content
    assert b"Test street, Los Angeles, CA" in response.content


def test_letting_detail_view(client):
    """
    Test the letting detail view.
    :param client: The test client.
    """

    # create a fake address
    fake_address = Address.objects.create(
        number=123,
        street='Test street',
        city='Los Angeles',
        state='CA',
        zip_code='90001'
    )


    # Create a test letting
    letting = Letting.objects.create(
        title='My Letting',
        address=fake_address,
    )

    # Get the response from the letting detail view
    url = reverse('lettings:letting', args=[letting.id])
    response = client.get(url)

    # Check that the response is 200 OK
    assert response.status_code == 200

    # Check that the letting details are in the context
    assert b"My Letting" in response.content
    assert b"Test street, Los Angeles, CA" in response.content
