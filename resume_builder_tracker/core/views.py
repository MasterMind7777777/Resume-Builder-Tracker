from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Add logic to retrieve data or perform actions for the dashboard
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'core/dashboard.html', context)