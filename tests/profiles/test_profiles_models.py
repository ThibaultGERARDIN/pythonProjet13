import pytest


@pytest.mark.django_db
def test_profile_str(profile):
    assert str(profile) == "jdoe"
