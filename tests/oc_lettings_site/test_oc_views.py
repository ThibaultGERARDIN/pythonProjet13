import pytest
from django.test import override_settings
from django.urls import path, reverse, include
from pytest_django.asserts import assertTemplateUsed
from oc_lettings_site import views as site_views


@pytest.mark.django_db
def test_root_index_view(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")


def test_admin_view_accessible(client):
    response = client.get("/admin/")
    # redirect to login if not logged in
    assert response.status_code in [200, 302]


# --- Custom 500 trigger view ---
def trigger_500(request):
    raise Exception("Intentional error")


# --- Test-only URLConf ---
urlpatterns = [
    path("", site_views.index, name="index"),
    path("profiles/", include("profiles.urls", namespace="profiles")),
    path("lettings/", include("lettings.urls", namespace="lettings")),
    path("force-500/", trigger_500),
]

# Attach custom handlers
handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.handler500"


@pytest.mark.django_db
@override_settings(DEBUG=False, ROOT_URLCONF=__name__)
def test_custom_404_template(client):
    response = client.get("/non-existent-url/")
    assert response.status_code == 404
    assertTemplateUsed(response, "oc_lettings_site/404.html")


@pytest.mark.django_db
@override_settings(DEBUG=False, ROOT_URLCONF=__name__)
def test_custom_500_template(client):
    # Don't raise view exceptions — let Django render the 500 page
    client.raise_request_exception = False
    response = client.get("/force-500/")
    assert response.status_code == 500
    assertTemplateUsed(response, "oc_lettings_site/500.html")
