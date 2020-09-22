from django.shortcuts import render
from home_page.models import Owner, Education, Skills, WorkExperience, ProgrammingApplication, Project

# Create your views here.
def home_index(request):
    owner = Owner.objects.get(name="Kyle Gonzalez")
    education = Education.objects.get(name="Arizona State University")
    skills = Skills.objects.all()
    programmingApplications = ProgrammingApplication.objects.all()
    workExperiences = WorkExperience.objects.all()
    context = {
        'owner': owner,
        'education': education,
        'skills': skills,
        'programming_applications': programmingApplications,
        'work_experiences': workExperiences,
    }

    return render(request, "index.html", context)

def experience_detail(request, pk):
    experience = WorkExperience.objects.get(pk=pk)
    context = {
        'experience': experience
    }
    return render(request, 'experience_detail.html', context)

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


