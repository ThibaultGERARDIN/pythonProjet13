import pytest
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


@pytest.fixture
def address():
    return Address.objects.create(
        number=10,
        street="Main Street",
        city="Lyon",
        state="LY",
        zip_code=69000,
        country_iso_code="FRA",
    )


@pytest.fixture
def letting(address):
    return Letting.objects.create(title="Cozy Flat", address=address)


@pytest.fixture
def user():
    return User.objects.create_user(
        username="jdoe",
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="secret",
    )


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user, favorite_city="Paris")
