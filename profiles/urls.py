from django.urls import path

from profiles.views.profile import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
