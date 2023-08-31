from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Lesson


# Create your views here.
class IndexView(ListView):
    model = Lesson
    template_name = 'lessons/index.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/detail.html'
    context_object_name = 'lesson'
