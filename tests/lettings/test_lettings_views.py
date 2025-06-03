import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_detail(client, letting):
    url = reverse("lettings:letting", args=[letting.id])
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
