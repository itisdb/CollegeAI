from django.shortcuts import render
from profiles.models import Profile
from tracker.models import tracker

def function(request, curr_page, page_from):
    if request.user.is_authenticated():
        profile = Profile.objects.get(user = request.user)
        obj = tracker(profile = profile,ip_address = , curr_page=curr_page,page_from = page_from)
        obj.save()