import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_detail(client, profile):
    url = reverse("profiles:profile", args=[profile.user.username])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
