from django.contrib import admin

from exam.models import Exam,ExamGenres
# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', )
    model = Exam


admin.site.register(Exam)
admin.site.register(ExamGenres)

