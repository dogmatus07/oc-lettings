from django.shortcuts import render


def index(request):
    """
    View function for the index page.
    :param request:
    :return: index.html
    """
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """
    Custom 404 error handler
    :param request:http request
    :param exception: exception raised
    :return:rendered 404 error page
    """
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Custom 500 error handler
    :param request: http request
    :return: rendered 500 error page
    """
    return render(request, '500.html', status=500)
