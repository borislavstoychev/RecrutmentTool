from django.db import models


# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recruiter(models.Model):
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=50)
    level = models.PositiveIntegerField(default=1)
    interviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.last_name


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    birth_date = models.DateField()
    skills = models.ManyToManyField(Skills)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField()
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.title


class Interview(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return f'Interview for {self.job.title}'


from .signals import *
