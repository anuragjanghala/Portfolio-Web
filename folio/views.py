from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Project, Message
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


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('landing-page')
        
    context= { 'form': form }
    return render(request, 'folio/project_form.html', context)



def inbox(request):
    inbox = Message.objects.all().order_by('is_read')
    context = {'inbox': inbox}
    return render(request, 'folio/inbox.html', context)


def message(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'folio/message.html', context)