import pytest


@pytest.mark.django_db
def test_address_str(address):
    assert str(address) == "10 Main Street"


@pytest.mark.django_db
def test_letting_str(letting):
    assert str(letting) == "Cozy Flat"
