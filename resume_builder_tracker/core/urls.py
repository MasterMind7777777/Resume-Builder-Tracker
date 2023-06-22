from django.urls import path
from .views import dashboard

app_name = 'core'

urlpatterns = [
    path('', dashboard, name='dashboard')
    # Add other URLs for the core app here
]
