from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.forms import UserCreationForm
from .forms import ProjectForm, SetPlanForm
from .models import Project, SetPlan
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


def firstpg(request):
    return  render(request, 'firstpg.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) 
        if form.is_valid(): #入力に誤りがあるか確認
            new_user = form.save() #誤りがなければnew_userに情報を保存
            #バリデーションで検証されてOKだった情報がcleaned_dataにセットされ、そこからusernameを取得しinput_usernameに代入
            input_username = form.cleaned_data.get("username") 
            #バリデーションで検証されてOKだった情報がcleaned_dataにセットされ、そこからpassword1を取得しinput_passwordに代入　　　　　　　　　　　　　　　　　　　　　　　　　　　　
            input_password = form.cleaned_data.get("password1")
            #ユーザを認証する
            new_user = authenticate(username=input_username, password=input_password)
            login(request, new_user)
            return redirect('mypage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            Project = form.save(commit=False)
            Project.author = request.user
            Project.save()
            form.save()
            return redirect('mypage')
    else:
        form = ProjectForm()
    return render(request, 'project.html', {'form':form})


def mypage(request):
    projects = Project.objects.filter(build_date__lte=timezone.now()).order_by('due_date')
    post_pks = request.POST.getlist('delete')
    Project.objects.filter(pk__in=post_pks).delete()
    return render(request, 'mypage.html', {'projects':projects})



class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

def setplan(request):
    if request.method == "POST":
        form = SetPlanForm(request.POST)
        print(form.is_valid())
        print(type(request.POST["minute"]))
        if form.is_valid():
            Startset = form.save(commit=False)
            Startset.save()
            form.save()
            return redirect('setplan')
    else:
        form = SetPlanForm()
    return  render(request, 'setplan.html', {'form':form})