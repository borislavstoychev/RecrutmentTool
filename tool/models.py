from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    birth_date = models.DateField()
    skills = models.ManyToManyField(Skills)
    recruiter = models.CharField(max_length=10)

    def __str__(self):
        return self.email


class Recruiter(models.Model):
    username = models.CharField(max_length=10, unique=True)
    level = models.PositiveIntegerField(default=1)
    interviews = models.PositiveIntegerField(default=0)


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField()
    skills = models.ManyToManyField(Skills)


class Interview(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)


from .signals import *
