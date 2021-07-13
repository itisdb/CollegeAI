from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from college.models import College,CollegeGenres,CollegeFacilities


class SEOCollegesView(View):

    def get(self, request, location):
        ulocation = location
        location = location.replace('-', ' ')
        colleges = College.objects.filter(
            Q(state__iexact=location) |
            Q(city__iexact=location) 
        ).order_by('created_at')
        context = {
            'colleges': colleges,
            'location': location,
            'ulocation': ulocation,
        }
        # ar = CollegeGenres.objects.filter(name = 'arts')
        # print(ar)
        # print(ar[0].college_set.all())
        # print(colleges[0].tags.all())
        return render(request, 'v2/pages/public/temporary/colleges.html', context)


class tagCollegesView(View):
    def get(self, request, tag):
        u_tag = tag
        tag = tag.replace('-',' ')
        ar = CollegeGenres.objects.filter(name__iexact = tag)
        if ar:
            colleges = ar[0].college_set.all()
        else:
            colleges = None
        context = {
            'colleges': colleges,
            'tag': ar[0],
            'utag': u_tag,
        }
        return render(request, 'v2/pages/public/temporary/tagcolleges.html', context)


class taglocCollegesView(View):
    def get(self, request, tag, location):
        u_tag = tag
        tag = tag.replace('-',' ')

        ulocation = location
        location = location.replace('-', ' ')


        ar = CollegeGenres.objects.filter(name__iexact = tag)
        if ar:
            colleges = ar[0].college_set.filter(Q(state__iexact=location) |
            Q(city__iexact=location)).order_by('created_at')
        else:
            colleges = None
        
        print(colleges)    
        context = {
            'colleges': colleges,
            'tag': ar[0],
            'utag': u_tag,
            'location': location,
            'ulocation': ulocation,
        }
        return render(request, 'v2/pages/public/temporary/tagloccolleges.html', context)

class topCollegesView(View):
    def get(self, request, college):
        ucollege = college
        college = college.replace('-',' ')
        colleges = College.objects.filter(
            Q(meta_keywords__1__iexact = college)
        ).order_by('created_at')
        context = {
            'colleges': colleges,
            'college': college,
            'ucollege': ucollege,
        }
        return render(request, 'v2/pages/public/temporary/topcolleges.html', context)