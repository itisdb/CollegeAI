"""Public views for colleges."""
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from base.constants import SUCCESS_ALERT_KEY

from college.models import College

from reviews.models import Review


class IndividualCollegeView(DetailView):

    model = College
    context_object_name = 'college'
    template_name = 'v2/pages/public/college.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(college=self.object)[:20]
        return context

    def post(self, request, *args, **kwargs):
        """Add reviews to a college."""
        college = College.objects.get(
            slug=request.POST.get('college_slug')
        )
        profile = request.user.profile
        Review.objects.create(
            college=college,
            comment=request.POST.get('comment'),
            name=profile.user.get_full_name(),
            source=Review.ReviewSources.SELF.value,
            profile=profile
        )
        return self.render_to_response({
            SUCCESS_ALERT_KEY: 'Your suggestion is being reviewed by AI.'
        })


class CollegesView(ListView):

    model = College
    template_name = 'v2/pages/public/colleges.html'
    context_object_name = 'colleges'
    paginate_by = 20
