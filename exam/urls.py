from collections import namedtuple
from django.urls import path

from exam.views.public import IndividualExamView,ExamsView

urlpatterns = [
    path('list/', ExamsView.as_view(), name='list'),
    path('<slug>/', IndividualExamView.as_view(), name='individual'),
] 