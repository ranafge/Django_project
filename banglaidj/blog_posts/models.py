from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    roll = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    class_of_student = models.CharField(max_length=25)

    def __repr(self):
        return self.name


