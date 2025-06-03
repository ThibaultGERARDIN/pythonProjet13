from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa.
# Integer est nunc, pulvinar a tempor et, bibendum id arcu.
# Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Render the index page displaying a list of all lettings.

    Retrieves all Letting objects from the database and passes them to the
    template context to be rendered in a list format.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page showing all available lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend.
# Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor,
# est ut luctus congue,
# dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Render the detail page for a specific letting.

    Retrieves a Letting instance by its ID and passes its title and associated
    address to the template context for rendering.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The primary key of the Letting to retrieve.

    Returns:
        HttpResponse: The rendered HTML page for the specified letting.

    Raises:
        Letting.DoesNotExist: If no Letting with the given ID is found.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
