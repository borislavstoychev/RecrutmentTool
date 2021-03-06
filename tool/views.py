# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets, status
from tool.helpers import create_interview, recruiter_checker, skills_checker
from tool.models import Candidate, Job, Recruiter, Skills, Interview
from tool.serializers import CandidateSerializer, JobSerializer, RecruiterSerializer, SkillsSerializer, \
    InterviewSerializer


class CandidatesViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        recruiter = recruiter_checker(data['recruiter'])
        new_candidate = Candidate.objects.create(first_name=data['first_name'],
                                                 last_name=data['last_name'],
                                                 email=data['email'],
                                                 bio=data['bio'],
                                                 birth_date=data['birth_date'],
                                                 recruiter=recruiter
                                                 )
        new_candidate.save()
        skills_checker(data, new_candidate)
        serializer = CandidateSerializer(new_candidate)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = request.data
        candidate = self.get_object()
        candidate.skills.clear()
        skills_checker(data, candidate)
        if candidate.recruiter.email != data['recruiter']['email']:
            recruiter = Recruiter.objects.get(email=candidate.recruiter.email)
            recruiter.level -= 1
            recruiter.save()
            new_recruiter = recruiter_checker(data['recruiter'])
            candidate.recruiter = new_recruiter
            candidate.save()
        return super().update(request)


class JobViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get_queryset(self):
        skill_name = self.request.query_params
        if skill_name:
            skill = skill_name.get('skill')
            queryset = Job.objects.filter(skills__name__contains=skill)
        else:
            queryset = Job.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        new_job = Job.objects.create(title=data['title'],
                                     description=data['description'],
                                     salary=data['salary'])
        new_job.save()
        skills_checker(data, new_job)
        create_interview(new_job)
        serializer = JobSerializer(new_job)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RecruiterView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

    def get_queryset(self):
        if self.request.query_params:
            level = self.request.query_params.get('level')
            queryset = Recruiter.objects.filter(level=level)
        else:
            queryset = Recruiter.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SkillsView(APIView):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.get(pk=kwargs['pk']))
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActiveSkills(APIView):

    def get(self, request, *args, **kwargs):
        skill = set(Skills.objects.filter(candidate__skills__in=Skills.objects.all()))
        serializer = SkillsSerializer(skill, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterviewView(APIView):
    def get(self, request, *args, **kwargs):
        interviews = Interview.objects.all()
        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
