from django.shortcuts import render

from college.models import College


def custom_not_found_error(request, *args, **argv):
    response = render(request, 'pages/error/404.html')
    response.status_code = 404
    return response


def custom_internal_error(request, *args, **argv):
    response = render(request, 'pages/error/404.html')
    response.status_code = 500
    return response


def home(request):
    colleges = College.objects.filter(
        is_top=True,
    )[:9]
    return render(request, 'v2/pages/public/home.html', {
        'colleges': colleges
    })
