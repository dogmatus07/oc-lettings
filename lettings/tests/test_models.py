import pytest
from lettings.models import Letting
from lettings.tests.tests_data import create_fake_address


@pytest.mark.django_db
def test_letting_str():
    """
    Test the __str__ method of the Letting model.
    :return:
    """

    #create fake address
    fake_address = create_fake_address()

    letting = Letting.objects.create(
        title='My Letting',
        address=fake_address,
    )
    assert str(letting) == 'My Letting'
    assert str(letting.address) == '123 Test St, Los Angeles, CA, 90001'


@pytest.mark.django_db
def test_letting_address():
    """
    Test the address of the Letting model.
    :return:
    """

    #create fake address
    fake_address = create_fake_address()

    letting = Letting.objects.create(
        title='My Letting',
        address=fake_address,
    )
    assert letting.address.number == 123
    assert letting.address.street == 'Test St'
    assert letting.address.city == 'Los Angeles'
    assert letting.address.state == 'CA'
    assert letting.address.zip_code == 90001
