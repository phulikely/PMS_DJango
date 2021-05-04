from django.shortcuts import render
from login.models import Project

# Create your views here.
def project_index(req):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    #return render(req, 'project_index.html', context)
    return ('This is project Index Page')

def project_detail(req, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(req, 'project_detail.html', context)