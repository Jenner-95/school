from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE) 
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
            return self.name

class Notes(models.Model):
    score = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.get_full_description()

    def get_full_description(self):
        return '{} / {} / {}'.format(self.student.get_full_name(), self.course, self.score)