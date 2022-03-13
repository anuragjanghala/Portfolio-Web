from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, 'folio/main.html', {'projects': projects})