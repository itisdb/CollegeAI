from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.db.models import Q

from college.models import College,CollegeGenres
from exam.models import Exam
from course.models import Course


from profiles.models import Psychometry, Profile


def custom_not_found_error(request, *args, **argv):
    response = render(request, 'v2/pages/error/404.html')
    response.status_code = 404
    return response


def custom_internal_error(request, *args, **argv):
    response = render(request, 'pages/error/500.html')
    response.status_code = 500
    return response


def home(request):
    colleges = College.objects.filter(is_top=True)[:6]
    exams = Exam.objects.filter(is_top=True)[:6]
    courses = Course.objects.filter(is_top=True)[:6]
    college_tags = CollegeGenres.objects.all().order_by('created_at')
    return render(request, 'v2/pages/public/home.html', {
        'colleges': colleges,
        'exams': exams,
        'courses': courses,
        'college_tags': college_tags
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

class CompareView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'v2/pages/public/comparef.html')

    def post(self, request, *args, **kwargs):
        first_col = request.POST['first_col']
        second_col = request.POST['second_col']
        third_col = request.POST['third_col']
        fourth_col = request.POST['fourth_col']
        compare_College = (College.objects.filter(Q(full_name=first_col) | Q(full_name=second_col) | Q(abbreviated_name=first_col) | Q(abbreviated_name = second_col) | Q(full_name=third_col) | Q(abbreviated_name=third_col) | Q(full_name=fourth_col) | Q(abbreviated_name=fourth_col)))
        return render(request, 'v2/pages/public/compare.html', {
            'colleges': compare_College
        })

