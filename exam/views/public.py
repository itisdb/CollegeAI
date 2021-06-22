from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from exam.models import Exam


class IndividualExamView(DetailView):
    model = Exam
    context_object_name = 'exam'
    template_name = 'v2/pages/public/exam.html'
        

class ExamsView(ListView):

    model = Exam
    template_name = 'v2/pages/public/exams.html'
    context_object_name = 'exams'
    paginate_by = 21

    def get_queryset(self):
        name = self.request.GET.get('search')
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(
                Q(full_name__icontains=name) |
                Q(abbreviated_name__icontains=name) |
                Q(exam_level__icontains=name) |
                Q(conducting_body__icontains=name)
            )
        return object_list