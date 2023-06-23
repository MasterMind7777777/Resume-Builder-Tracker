from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    educations = models.ManyToManyField('Education', blank=True)
    experiences = models.ManyToManyField('Experience', blank=True)
    contact_information = models.ManyToManyField('ContactInformation', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=100, help_text="Name of the educational institution")
    degree = models.CharField(max_length=100, help_text="Degree or qualification achieved")
    field_of_study = models.CharField(max_length=100, help_text="Field of study or major")
    graduation_year = models.PositiveIntegerField(blank=True, null=True, help_text="Year of graduation")
    honors = models.CharField(blank=True, max_length=100, help_text="Honors or distinctions received")
    description = models.TextField(blank=True, help_text="Additional details or description of the education")

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=100, help_text="Name of the company or organization")
    position = models.CharField(max_length=100, help_text="Job position or title")
    responsibilities = models.TextField(blank=True, help_text="Responsibilities or tasks performed")
    location = models.CharField(blank=True, max_length=100, help_text="Location of the company or organization")
    start_date = models.DateField(blank=True, null=True, help_text="Start date of the experience")
    end_date = models.DateField(blank=True, null=True, help_text="End date of the experience")
    description = models.TextField(blank=True, help_text="Additional details or description of the experience")

    def __str__(self):
        return f"{self.position} at {self.company}"


PROFICIENCY_CHOICES = [
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
]

class Skill(models.Model):
    name = models.CharField(max_length=100, help_text="Name or title of the skill")
    description = models.TextField(blank=True,help_text="Brief description or additional details about the skill")
    years_of_experience = models.PositiveIntegerField(blank=True, null=True, help_text="Number of years of experience in the skill")
    proficiency_level = models.CharField(
        blank=True,
        max_length=50,
        choices=PROFICIENCY_CHOICES,
        help_text="Proficiency level in the skill (Choose from the provided options)"
    )

    def __str__(self):
        return self.name


class ContactInformation(models.Model):
    full_name = models.CharField(max_length=100, help_text="Full name of the individual")
    contact_info = models.TextField(blank=True, help_text="Summary or description of the contact information")
    phone_number = models.CharField(blank=True, max_length=20, help_text="Phone number")
    email = models.EmailField(blank=True, help_text="Email address")
    address = models.CharField(blank=True, max_length=100, help_text="Physical address")
    website = models.URLField(blank=True, help_text="Personal website URL")
    linkedin = models.URLField(blank=True, help_text="LinkedIn profile URL")
    twitter = models.URLField(blank=True, help_text="Twitter profile URL")
    github = models.URLField(blank=True, help_text="GitHub profile URL")

