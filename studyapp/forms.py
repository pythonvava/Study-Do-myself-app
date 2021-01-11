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
                    'pattern':'[0-9]',
                    }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':"form-control",
                    'placeholder':'description (概要)',
                    }
            ),
            'due_date': forms.SelectDateWidget(
                attrs={
                    'class':"form-control",
                    }
            ),
        }


class SetPlanForm(forms.ModelForm):

    class Meta:
        model = SetPlan
        labels = {
            'minute':'',
            'count':'',
            'sumtime':'',
        }
        fields = ('minute', 'count', 'sumtime',)
        widgets = {
            'minute' : forms.Select(
                attrs={
                    'class':"form-control",
                    'palceholder':'minute（分/セット）',
                }
            ),
            'count' : forms.DateInput(
                attrs={
                    'class':"form-control",
                    'palceholder':'set（セット）',
                }
            ),
            'sumtime' : forms.DateInput(
                attrs={
                    'class':"form-control",
                    'palceholder':'sumtime（合計）',
                }
            ),
        }