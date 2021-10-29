from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from rest_framework.fields import DictField, CharField

from tool.models import Candidate, Job, Skills, Recruiter, Interview


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ('recruiter', )
        depth = 1


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
        depth = 1


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = "__all__"


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"
        depth = 1
