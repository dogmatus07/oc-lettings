import logging
from django.http import HttpResponse
from django.shortcuts import render
import sentry_sdk


logger = logging.getLogger(__name__)


def index(request):
    """
    View function for the index page.
    :param request:
    :return: index.html
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
    :param request:http request
    :param exception: exception raised
    :return:rendered 404 error page
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
    :param request: http request
    :return: rendered 500 error page
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
    :param request:
    :return:
    """

    try:
        result = 1/0
        return HttpResponse(f'Result : {result}')
    except Exception as e:
        logger.error("An error occurred: %s", e)
        sentry_sdk.capture_exception(e)
        return HttpResponse("An error occurred, and it has been logged.", status=500)
