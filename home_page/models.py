from django.db import models
from datetime import datetime

# Create your models here.
class Owner(models.Model):
    name = models.TextField(default="Name")
    generalAboutMe = models.TextField(default="About me")
    image = models.ImageField(upload_to='owner_image')

class Education(models.Model):
    name = models.TextField(default="School name")
    dateStarted = models.DateTimeField(auto_now=False)
    dateEnded = models.DateTimeField(auto_now=False)
    description = models.TextField(default="School description")
    image = models.ImageField(upload_to='education_image')
    owner = models.ForeignKey('Owner', related_name="education", on_delete=models.CASCADE)

class Skills(models.Model):
    name = models.TextField(default="Skill name")
    image = models.ImageField(upload_to='skill_image', default="")
    owner = models.ForeignKey('Owner', related_name="skills", on_delete=models.CASCADE)

class ProgrammingApplication(models.Model):
    name = models.TextField(default="Application name")
    image = models.ImageField(upload_to='application_image', default="")
    owner = models.ForeignKey('Owner', related_name='programming_application', on_delete=models.CASCADE)

class WorkExperience(models.Model):
    name = models.TextField(default="Name")
    dateStarted = models.DateTimeField(auto_now=False)
    dateEnded = models.DateTimeField(auto_now=False)
    description = models.TextField(default="Experience Description")
    skillsUsed = models.TextField(default="Skills used")
    image = models.ImageField(upload_to='work_image')
    owner = models.ForeignKey('Owner', related_name="work_experiences", on_delete=models.CASCADE)

class Project(models.Model):
    title = models.TextField(default="Title")
    description = models.TextField(default="Description")
    summary = models.TextField(default="Summary description")
    programmingLanguages = models.TextField(default="Description")
    image = models.ImageField(upload_to="project_image")