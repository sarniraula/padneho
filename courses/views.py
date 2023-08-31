from django.views.generic import ListView, DetailView
from .models import Course


# Create your views here.
class AllCoursesView(ListView):
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'
