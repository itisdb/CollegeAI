from collections import namedtuple
from django.urls import path

from course.views.public import IndividualCourseView,CoursesView

urlpatterns = [
    path('list/', CoursesView.as_view(), name='list'),
    path('<slug>/', IndividualCourseView.as_view(), name='individual'),
] 