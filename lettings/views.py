import logging
import sentry_sdk
from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the letting index page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page (lettings/index.html)

    Raises:
        Exception: If an error occurs while retrieving lettings or rendering the page.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error("An error occurred while rendering the index page: %s", e)
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)


def letting(request, letting_id):
    """
    View function for a specific letting.

    Args:
        request: The HTTP request object.
        letting_id: The ID of the letting to retrieve.

    Returns:
         HttpResponse: Rendered HTML page (lettings/letting.html)

    Raises:
        Exception: If an error occurs while retrieving the letting or rendering the page.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error("Error in rendering the letting detail view,"
                     "ID: %s, Error: %s", letting_id, e)
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)
