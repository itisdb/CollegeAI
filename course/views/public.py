from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from course.models import Course


class IndividualCourseView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'v2/pages/public/course.html'

    def get_context_data(self, **kwargs):
        row_limit = 2
        context = super().get_context_data(**kwargs)
        syllabus = []
        syllabus_tuple = []

        for index, degree in enumerate(self.object.syllabus):
            syllabus_tuple.append(degree)

            if (index + 1) % row_limit == 0:
                syllabus.append(syllabus_tuple)
                syllabus_tuple = []

        if syllabus_tuple:
            syllabus.append(syllabus_tuple)

        context['syllabus'] = syllabus

        career = []
        career_tuple = []

        for index, degree in enumerate(self.object.career):
            career_tuple.append(degree)

            if (index + 1) % row_limit == 0:
                career.append(career_tuple)
                career_tuple = []

        if career_tuple:
            career.append(career_tuple)

        context['career'] = career

        top_institutes = []
        top_institutes_tuple = []

        for index, degree in enumerate(self.object.top_institutes):
            top_institutes_tuple.append(degree)

            if (index + 1) % row_limit == 0:
                top_institutes.append(top_institutes_tuple)
                top_institutes_tuple = []

        if top_institutes_tuple:
            top_institutes.append(top_institutes_tuple)

        context['top_institutes'] = top_institutes        
        return context


        

class CoursesView(ListView):

    model = Course
    template_name = 'v2/pages/public/courses.html'
    context_object_name = 'courses'
    paginate_by = 21

    def get_queryset(self):
        name = self.request.GET.get('search')
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(
                Q(full_name__icontains=name) |
                Q(abbreviated_name__icontains=name) |
                Q(degree_name__icontains=name) |
                Q(stream__icontains=name)
            )
        return object_list