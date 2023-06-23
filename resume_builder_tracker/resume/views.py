from django.shortcuts import render
from .models import Resume

def resume_view(request, resume_id):
    # Retrieve the resume object from the database
    resume = Resume.objects.get(id=resume_id)
    # Pass the resume object to the template
    context = {
        'resume': resume
    }

    return render(request, 'resume/resume_template.html', context)
