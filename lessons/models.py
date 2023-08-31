from django.db import models
from courses.models import Course

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    lesson_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
