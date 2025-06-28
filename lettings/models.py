from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """
    Address model representing a physical address.

    Args:
        number (int): The house or building number.
        street (str): The street name.
        city (str): The city name.
        state (str): The state abbreviation (2 characters).
        zip_code (int): The postal code.
        country_iso_code (str): The ISO code of the country (3 characters).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        String representation of the Address model.

        Returns:
            str: A string representation of the address in the format "number street".
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta class for Address model to define ordering.
        """
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

class Letting(models.Model):
    """
    Letting model representing a property for rent.

    Args:
        title (str): The title of the letting.
        address (Address): A one-to-one relationship with the Address model.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Letting model.

        Returns:
            str: The title of the letting.
        """
        return self.title
