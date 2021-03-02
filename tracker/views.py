from django.shortcuts import render
from tracker.models import tracker
from tracker.utilities import get_client_ip

def log_to_tracker(request, curr_pages):
    if request.user.is_authenticated():
        profile = request.user.profile
        ip = get_client_ip(request)
        obj = Tracker.objects.create(profile = profile,ip_address = ip, curr_page=curr_pages)
        obj.save()