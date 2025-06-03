from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis
# leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Render the main index page of the site.

    This view serves as the homepage and renders a static or navigational landing page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML for the site's homepage.
    """
    return render(request, "oc_lettings_site/index.html")


def handler404(request, exception, template_name="oc_lettings_site/404.html"):
    """
    Custom handler for HTTP 404 (Page Not Found) errors.

    Renders a user-friendly 404 error page when a requested URL is not found.

    Args:
        request (HttpRequest): The HTTP request that caused the error.
        exception (Exception): The exception raised.
        template_name (str): Path to the 404 template.

    Returns:
        HttpResponse: A rendered 404 error page with a 404 status code.
    """
    return render(request, template_name, status=404)


def handler500(request, template_name="oc_lettings_site/500.html"):
    """
    Custom handler for HTTP 500 (Server Error) responses.

    Renders a user-friendly 500 error page when an unhandled exception occurs.

    Args:
        request (HttpRequest): The HTTP request that caused the error.
        template_name (str): Path to the 500 template.

    Returns:
        HttpResponse: A rendered 500 error page with a 500 status code.
    """
    return render(request, template_name, status=500)
