from django.shortcuts import render, redirect
from django.views.generic.base import View


from college.models import College

from profiles.models import Psychometry, Profile

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

class PsychoView(View): 
    def get(self, request, *args, **kwargs):
        if request.user.id:
            return render(request, 'v2/pages/public/psychometric.html')
        else:
            return render(request, 'v2/pages/public/home.html', {'error': 'You need to login in order to give the exam'})

    def post(self, request, *args, **kwargs):
        placement = request.POST['placement']
        infrastructure = request.POST['infrastructure']
        academics = request.POST['academics']
        psycho_obj = Psychometry.objects.filter(profile= request.user.profile).first()
        if  psycho_obj:
            psycho_obj.infrastructure = infrastructure
            psycho_obj.academics = academics
            psycho_obj.placement = placement
            psycho_obj.save()
        else:
            psycho_obj = Psychometry.objects.create(
                profile= request.user.profile, 
                infrastructure = infrastructure,
                academics=academics,
                placement=placement)
            psycho_obj.save()
        return redirect('/', {'message': 'Your test was succesful, we will contact you soon'})


def compare(request):
    colleges = College.objects.all()[0:4]
    return render(request, 'v2/pages/public/compare.html', {
        'colleges': colleges
    })