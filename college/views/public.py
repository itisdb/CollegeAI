"""Public views for colleges."""
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from base.constants import SUCCESS_ALERT_KEY

from college.models import College, CollegeBookmark, AppliedCollege
from leads.controllers.direct_lead_handler import ApplyCollegeHandler

from reviews.models import Review


class IndividualCollegeView(DetailView):

    model = College
    context_object_name = 'college'
    template_name = 'v2/pages/public/college.html'

    def get_queryset(self):
        return College.objects.all().order_by('created_at')

    def get_context_data(self, **kwargs):
        row_limit = 3

        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(college=self.object)[:20]

        if getattr(self.request.user, 'profile', None):
            context['is_applied'] = AppliedCollege.objects.filter(
                profile=self.request.user.profile,
                college=self.object
            ).exists()
            context['is_bookmarked'] = CollegeBookmark.objects.filter(
                profile=self.request.user.profile,
                college=self.object
            ).exists()

        degrees = []
        degree_tuple = []

        for index, degree in enumerate(self.object.degree):
            degree_tuple.append(degree)

            if (index + 1) % row_limit == 0:
                degrees.append(degree_tuple)
                degree_tuple = []

        if degree_tuple:
            degrees.append(degree_tuple)

        context['degrees'] = degrees
        context['admission_procedures'] = (
            self.object.admission_procedure.split('-')
            if self.object.admission_procedure
            else None
        )
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
    paginate_by = 21

    def get_queryset(self):
        name = self.request.GET.get('search')
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(
                Q(full_name__icontains=name) |
                Q(abbreviated_name__icontains=name) |
                Q(state__icontains=name) |
                Q(city__icontains=name)
            )
        return object_list


class AddBookmarkView(View):

    def get(self, request, slug: str):
        college = College.objects.get(slug=slug)
        profile = request.user.profile
        try:
            CollegeBookmark.objects.create(
                college=college,
                profile=profile
            )
            return redirect('profile:dashboard')
        except BaseException:
            CollegeBookmark.objects.get(
                college=college,
                profile=profile
            ).delete()
            return redirect(request.META['HTTP_REFERER'])


class ApplyCollegeView(View):

    def get(self, request, college_uuid: str):
        is_done, college = ApplyCollegeHandler().store(request.user.profile, college_uuid)
        return redirect('college:individual', college.slug)
