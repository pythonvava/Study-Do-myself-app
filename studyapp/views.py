from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.forms import UserCreationForm
from .forms import ProjectForm


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
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            form.save()
            return redirect('firstpg')
    else:
        form = ProjectForm()
    return render(request, 'project.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')