from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='user')),
    path('', include('core.urls', namespace='core')),
    path('resume/', include('resume.urls', namespace='resume')),
    path('api/v1/', include('api_v1.urls', namespace='api_v1')),
    
]
