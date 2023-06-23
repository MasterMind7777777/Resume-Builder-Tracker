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

def generate_resume(request, resume_id):
    # Retrieve the necessary data from your models or any other source
    resume = Resume.objects.get(id=resume_id)

    # Define an array or list of available information sections
    info_sections = [
        {'include': True, 'template': 'resume/blocks/base/personal_info.html'},
        {'include': True, 'template': 'resume/blocks/base/education.html'},
        {'include': True, 'template': 'resume/blocks/base/experience.html'},
        {'include': True, 'template': 'resume/blocks/base/skills.html'},
    ]

    # Render the HTML template with the context
    return render(request, 'resume/layouts/base_layout.html', {
        'resume': resume,
        'info_sections': info_sections,
    })

def adjust_layout(request, resume_id):
    # Retrieve the necessary data from your models or any other source
    resume = Resume.objects.get(id=resume_id)

    # Define an array or list of available information sections
    info_sections = [
        {'include': True, 'template': 'resume/blocks/base/personal_info.html'},
        {'include': True, 'template': 'resume/blocks/base/education.html'},
        {'include': False, 'template': 'resume/blocks/base/experience.html'},
        {'include': False, 'template': 'resume/blocks/base/skills.html'},
    ]

    # Render the HTML template with the context
    context = {
        'resume': resume,
        'info_sections': info_sections,
    }

    return render(request, 'resume/layouts/adjust_layout.html', context)

