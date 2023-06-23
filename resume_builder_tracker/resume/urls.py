from django.urls import path
from .views import resume_view

app_name = 'resume'  # Replace 'resume' with the name of your app

urlpatterns = [
    path('<int:resume_id>/', resume_view, name='resume_view'),
    # Add more URL patterns if needed
]
