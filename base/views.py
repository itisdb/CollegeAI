from django.shortcuts import render


def custom_not_found_error(request, *args, **argv):
    response = render(request, 'pages/error/404.html')
    response.status_code = 404
    return response


def custom_internal_error(request, *args, **argv):
    response = render(request, 'pages/error/404.html')
    response.status_code = 500
    return response
