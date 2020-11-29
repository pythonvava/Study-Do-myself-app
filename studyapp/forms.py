from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
        
    class Meta:
        model = Project
        labels = {
            'project_name':'',
            'expenses_item':'',
            'expenses':'',
            'description':'',
        }
        fields = ('project_name', 'expenses_item', 'expenses', 'description', )
        widgets = {
            'project_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'pjroject_name (プロジェクト名)',
                    }
            ),
            'expenses_item': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'placeholder':'expenses_item (経費項目)',
                    }
            ),
            'expenses': forms.TextInput(
                attrs={
                    'class':"form-control",
                    'placeholder':'expenses (経費)',
                    }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':"form-control",
                    'placeholder':'description (概要)',
                    }
            ),
        }