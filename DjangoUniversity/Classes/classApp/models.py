from django.db import models


class djangoClasses(models.Model):
    Title = models.CharField(max_length=25, default='', null=False)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=50, default='', null=False)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
