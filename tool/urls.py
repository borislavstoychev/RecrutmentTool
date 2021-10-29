from django.urls import path, include
from tool import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('candidates', views.CandidatesViewSet)
router.register('jobs', views.JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recruiters/', views.RecruiterView.as_view(), name="recruiters"),
    path('skills/<int:pk>/', views.SkillsView.as_view(), name="skills"),
    path('skills/active/', views.ActiveSkills.as_view(), name="active skills"),
    path('interviews/', views.InterviewView.as_view(), name="interviews"),
   ]