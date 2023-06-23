from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ResumeViewSet, EducationViewSet, ExperienceViewSet, SkillViewSet, ContactInformationViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact-information', ContactInformationViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]
