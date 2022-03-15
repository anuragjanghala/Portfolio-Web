from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm


# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'folio/main.html', {'projects': projects})


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'folio/project.html', context)


def addProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    context= { 'form': form }
    return render(request, 'folio/project_form.html', context)