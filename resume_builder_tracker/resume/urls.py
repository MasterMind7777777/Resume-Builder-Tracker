from django.urls import path
from .views import resume_view, generate_resume, adjust_layout

app_name = 'resume'  # Replace 'resume' with the name of your app

urlpatterns = [
    path('<int:resume_id>/', resume_view, name='resume_view'),
    path('<int:resume_id>/generate/', generate_resume, name='generate_resume'),
    path('<int:resume_id>/adjust/', adjust_layout, name='adjust_layout'),
    # Add more URL patterns if needed
]
