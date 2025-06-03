from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address associated with a letting.

    Fields:
        number (int): Street number, must be a positive integer ≤ 9999.
        street (str): Name of the street (max 64 characters).
        city (str): City name (max 64 characters).
        state (str): Two-letter state code.
        zip_code (int): Postal code, must be a positive integer ≤ 99999.
        country_iso_code (str): Three-letter ISO country code.

    Returns:
        str: A human-readable string representing the address.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting (rental) unit.

    Fields:
        title (str): A descriptive title for the letting (max 256 characters).
        address (Address): A one-to-one relationship to an Address object.

    Returns:
        str: The title of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
