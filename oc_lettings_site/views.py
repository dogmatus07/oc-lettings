import logging
from django.http import HttpResponse
from django.shortcuts import render
import sentry_sdk


logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page.

    Args:
        request: The HTTP request object.

    Returns:
        rendered index.html page or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs while rendering the index page.
    """
    try:
        return render(request, 'index.html')
    except Exception as e:
        logger.error("An error occurred while rendering the index page: %s", e)
        sentry_sdk.capture_exception(e)
        return HttpResponse("An error occurred while rendering the index page.", status=500)


def custom_404_view(request, exception):
    """
    Custom 404 error handler

    Args:
        request: The HTTP request object.
        exception: The exception raised (not used in this implementation).

    Returns:
        rendered 404.html page or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs while rendering the 404 page.
    """
    try:
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error("An error occurred while rendering the 404 page: %s", e)
        sentry_sdk.capture_exception(e)
        return HttpResponse("An error occurred while rendering the 404 page.", status=500)


def custom_500_view(request):
    """
    Custom 500 error handler

    Args:
        request: The HTTP request object.

    Returns:
        rendered 500.html page or an error message if an exception occurs.

    Raises:
        Exception: If an error occurs while rendering the 500 page.
    """
    try:
        return render(request, '500.html', status=500)
    except Exception as e:
        logger.error("An error occurred while rendering the 500 page: %s", e)
        sentry_sdk.capture_exception(e)
        return HttpResponse("An error occurred while rendering the 500 page.", status=500)


def simulate_error_view(request):
    """
    Simulate a server error

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response indicating the result of the simulated error.

    Raises:
        Exception: Always raises an exception to simulate a 500 server error.
    """

    try:
        result = 1/0
        return HttpResponse(f'Result : {result}')
    except Exception as e:
        logger.error("An error occurred: %s", e)
        sentry_sdk.capture_exception(e)
        return HttpResponse("An error occurred, and it has been logged.", status=500)
