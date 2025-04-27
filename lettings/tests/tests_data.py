import pytest
from lettings.models import Address


@pytest.mark.django_db
def create_fake_address():
    """
    Create a fake address for testing purposes.
    :return:
    """
    fake_address = Address.objects.create(
        id=1,
        number=123,
        street='Test street',
        city='Los Angeles',
        state='CA',
        zip_code='90001'
    )
    return fake_address
