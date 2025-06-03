from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat
# libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request):
    """
    Render the index page displaying a list of all user profiles.

    Retrieves all Profile instances from the database and passes them to the
    template context for rendering in a list format.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page showing all available user profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Render the profile detail page for a given user.

    Retrieves the Profile instance associated with the given username and
    passes it to the template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being requested.

    Returns:
        HttpResponse: The rendered HTML page for the user's profile.

    Raises:
        Profile.DoesNotExist: If no profile is found for the given username.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
