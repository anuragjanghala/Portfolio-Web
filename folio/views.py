from multiprocessing import context
from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'folio/main.html', {'projects': projects})


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'folio/project.html', context)