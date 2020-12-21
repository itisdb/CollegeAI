"""Public views for colleges."""
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from base.constants import SUCCESS_ALERT_KEY

from college.models import College

from reviews.models import Review


class IndividualCollegeView(View):

    def get(self, request, college_slug, *args, **kwargs):
        """Display single college."""
        college = College.objects.get(
            slug=college_slug
        )
        return render(
            request,
            'pages/public/college.html',
            {'college': college}
        )

    def post(self, request, college_slug, *args, **kwargs):
        """Add reviews to a college."""
        college = College.objects.get(
            slug=college_slug
        )
        profile = request.user.profile
        Review.objects.create(
            college=college,
            comment=request.POST.get('comment'),
            name=profile.user.get_full_name(),
            source=Review.ReviewSources.SELF.value,
            profile=profile
        )
        return render(
            request,
            'pages/public/college.html',
            {SUCCESS_ALERT_KEY: 'Your review is being reviewed by AI.'}
        )


class CollegesView(ListView):

    def get(self, request, *args, **kwargs):
        pass