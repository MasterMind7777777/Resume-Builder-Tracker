import os
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from resume.models import Resume, Education, Experience, Skill, ContactInformation
from .serializers import (
    UserSerializer,
    ResumeSerializer,
    EducationSerializer,
    ExperienceSerializer,
    SkillSerializer,
    ContactInformationSerializer,
)
from django.contrib.auth import get_user_model
User=get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @csrf_exempt
    def save_adjusted_layout(self, request, *args, **kwargs):
        if request.method == 'POST':
            layout_id = request.data.get('layout_id')
            adjusted_layout = request.data.get('adjusted_layout')
            user = request.user

            # Save the adjusted layout to a separate file
            file_path = f'/resume/layouts/{user}/adjusted_layout_{layout_id}.html'
            file_dir = os.path.dirname(file_path)
            os.makedirs(file_dir, exist_ok=True)

            with open(file_path, 'w') as file:
                file.write(adjusted_layout)

            response_data = {
                'message': 'Layout saved successfully!'
            }
            return JsonResponse(response_data)

        response_data = {
            'message': 'Invalid request!'
        }
        return JsonResponse(response_data, status=400)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)