from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class meta:
        model = Project
        fields = ('project_name', 'description')