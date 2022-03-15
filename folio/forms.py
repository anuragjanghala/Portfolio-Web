from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'description']
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})
        
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})