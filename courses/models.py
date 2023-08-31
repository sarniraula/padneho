from django.db import models


def get_course_thumbnail_path(instance, filename):
    return 'uploads/courses/thumbails/{instance.title}/{filename}'


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=get_course_thumbnail_path)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
