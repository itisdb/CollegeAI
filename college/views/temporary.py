from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from college.models import College


class SEOCollegesView(View):

    def get(self, request, location):
        location = location.replace('-', ' ')
        colleges = College.objects.filter(
            Q(state__icontains=location) |
            Q(city__icontains=location)
        ).order_by('created_at')
        context = {
            'colleges': colleges,
            'location': location,
        }
        return render(request, 'v2/pages/public/temporary/colleges.html', context)
