from django.urls import path

from profiles.views.profile import Dashboard

urlpatterns = [
    path('list/', Dashboard.as_view(), name='dashboard'),
]
