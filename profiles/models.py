from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Extends the built-in User model with additional profile information.

    Fields:
        user (User): A one-to-one relationship to Django's built-in User model.
        favorite_city (str): An optional field for the user's favorite city (max 64 characters).

    Returns:
        str: The username of the associated user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
