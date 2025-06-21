from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Profile model representing a user profile.

    Args:
        user (User): A one-to-one relationship with the User model.
        favorite_city (str): The user's favorite city, optional.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        String representation of the Profile model.

        Args:
            None

        Returns:
            str: The username of the user associated with the profile.
        """
        return self.user.username
