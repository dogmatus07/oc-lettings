import logging
import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the profiles index page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page (profiles/index.html) with a list of profiles.

    Raises:
        Exception: If an error occurs while retrieving profiles or rendering the page.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error("An error occurred while rendering the index page: %s", e)
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)


def profile(request, username):
    """
    View function for a specific profile.

    Args:
        request: The HTTP request object.
        username: The username of the profile to display.

    Returns:
        Rendered HTML page (profiles/profile.html) with the profile details.

    Raises:
        Exception: If an error occurs while retrieving the profile or rendering the page.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {
            'profile': profile,
            'favorite_city': profile.favorite_city,
        }
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error("Error in rendering the profile detail view,"
                     "Username: %s, Error: %s", username, e)
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)
