from django.shortcuts import render
from profiles.models import Profile
from tracker.models import tracker

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def function(request, curr_page, page_from):
    if request.user.is_authenticated():
        profile = Profile.objects.get(user = request.user)
        ip = get_client_ip(request)
        obj = tracker(profile = profile,ip_address = ip, curr_page=curr_page,page_from = page_from)
        obj.save()