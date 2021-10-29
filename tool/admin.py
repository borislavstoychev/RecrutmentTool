from django.contrib import admin

# Register your models here.
from tool.models import Candidate, Job, Recruiter, Skills

admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Recruiter)
admin.site.register(Skills)
