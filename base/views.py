from django.shortcuts import render, redirect

from college.models import College
from profiles.models import psychometry, Profile

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

def refer(request):
    return render(request, 'v2/pages/public/refer.html')

def about(request):
    return render(request, 'v2/pages/public/about.html')

def contact(request):
    return render(request, 'v2/pages/public/contact.html')

def career(request):
    return render(request, 'v2/pages/public/career.html')

def advertising(request):
    return render(request, 'v2/pages/public/advertising.html')

def terms(request):
    return render(request, 'v2/pages/public/terms.html')

def privacy(request):
    return render(request, 'v2/pages/public/privacy.html')

def psycho(request):
    if request.method == 'POST':
        placement = request.POST['placement']
        infrastructure = request.POST['infrastructure']
        academics = request.POST['academics']
        profile_obj = Profile.objects.get(user = request.user)
        if  psychometry.objects.get(profile=profile_obj):
            psycho_obj = psychometry.objects.get(profile=profile_obj)
            psycho_obj.infrastructure = infrastructure
            psycho_obj.academics = academics
            psycho_obj.placement = placement
            psycho_obj.save()
        else:
            psycho_obj = psychometry.objects.create(profile=profile_obj, infrastructure=infrastructure, academics=academics, placement=placement)
            psycho_obj.save()
        return redirect('/')
    else:
        return render(request, 'v2/pages/public/psychometric.html')
