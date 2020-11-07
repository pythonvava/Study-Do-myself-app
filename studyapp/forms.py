from django import forms
from .models import Signup, Signin, Project

class signupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ('username', 'password',)

class signinForm(forms.ModelForm):
    class Meta:
        model = Signin
        fields = ('username', 'password',)

class makeprojectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'due_date', 'description',)