import re
from django.core import paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View, ListView
from django.core.paginator import Paginator

from college.models import College,CollegeGenres,CollegeFacilities


class SEOCollegesView(View):
    def get(self, request, location):
        ulocation = location
        location = location.replace('-', ' ')
        colleges = College.objects.filter(
            Q(state__iexact=location) |
            Q(city__iexact=location) 
        ).order_by('created_at')
        paginator = Paginator(colleges, 21)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'colleges' : colleges,
            'location' : location,
            'ulocation' : ulocation,
            'page_obj' : page_obj
        }
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
        paginator = Paginator(colleges, 21)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'colleges': colleges,
            'tag': ar[0],
            'utag': u_tag,
            'page_obj': page_obj
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
        paginator = Paginator(colleges, 21)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number) 
        context = {
            'colleges': colleges,
            'tag': ar[0],
            'utag': u_tag,
            'location': location,
            'ulocation': ulocation,
            'page_obj': page_obj
        }
        return render(request, 'v2/pages/public/temporary/tagloccolleges.html', context)

class topCollegesView(View):
    def get(self, request, college):
        ucollege = college
        college = college.replace('-',' ')
        colleges = College.objects.filter(
            Q(meta_keywords__1__iexact = college)
        ).order_by('created_at')
        paginator = Paginator(colleges, 21)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'colleges': colleges,
            'college': college,
            'ucollege': ucollege,
            'page_obj': page_obj
        }
        return render(request, 'v2/pages/public/temporary/topcolleges.html', context)


class tagstreamCollegesView(View):
    def get(self, request, tag):
        utag = tag
        tag = tag.replace('-',' ')
        colleges = College.objects.filter(degree__contains = [tag])
        paginator = Paginator(colleges, 21)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'utag' : utag,
            'tag' : tag,
            'colleges' : colleges,
            'page_obj' : page_obj
        }
        return render(request, 'v2/pages/public/temporary/tagstreamcolleges.html', context)
