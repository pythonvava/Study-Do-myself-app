from django import forms
from .models import Project, SetPlan
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        labels = {
            'project_name':'',
            'expenses_item':'',
            'expenses':'',
            'description':'',
            'build_date':'',
            'due_date':'',
        }
        fields = ('project_name', 'expenses_item', 'expenses', 'description', 'build_date', 'due_date')
        widgets = {
            'project_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'pjroject_name',
                    }
            ),
            'expenses_item': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'expenses_item',
                    }
            ),
            'expenses': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'expenses',
                    'pattern':'[0-9]',
                    }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'description',
                    }
            ),
            'due_date': forms.SelectDateWidget(
                attrs={
                    'class':'form-control',
                    'style': 'width: 31%; display: inline-block; margin:3px;'
                    }
            ),
        }


class SetPlanForm(forms.ModelForm):

    class Meta:
        model = SetPlan
        labels = {
            'minute':'',
            'sets':'',
        }
        fields = ('minute', 'sets')
        widgets = {
            'minute' : forms.Select(
                attrs={
                    'class':'form-control',
                    'pattern':'^[0-9]+$',
                }
            ),
            'sets' : forms.Select(
                attrs={
                    'class':'form-control',
                    'pattern':'^[0-9]+$',
                }
            ),
        }

   