from pyexpat import model
from attr import fields
from django.contrib import admin
from django.forms import inlineformset_factory
# <HINT> Import any new Models here
from .models import Choice, Course, Lesson, Instructor, Learner, Question

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class ChoiceInLine(admin.StackedInline):
    model  = Choice


class QuestionInLine(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInLine]

# <HINT> Register Question and Choice models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)