from django.urls import path
from . import views

urlpatterns = [
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
]
