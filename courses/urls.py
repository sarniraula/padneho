from django.urls import path
from . import views

urlpatterns = [
    # path('courses', views.AllCoursesView.as_view(), name='courses-list'),

    # For now, home page is the course list page
    path('', views.AllCoursesView.as_view(), name='courses-list'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
]
