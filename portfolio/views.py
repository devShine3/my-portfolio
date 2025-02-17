from django.shortcuts import render
from .models import Experience, Project, Resume

# Create your views here.
def home(request):
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    resume = Resume.objects.last()
    return render(request, 'portfolio/home.html', {
        'experiences' : experiences,
        'projects' : projects,
        'resume' : resume
    })
