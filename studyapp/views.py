from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ProjectForm


def firstpg(request):
    return  render(request, 'firstpg.html')


def login(request):
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
            if new_user is not None:
                #ユーザをログイン状態にする
                login(request, new_user)
                return redirect('firstpg')
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    logout(request)
    return render(request, 'firstpg.html')


def project(request):
    form = ProjectForm
    return render(request, 'project.html', {'form':form})


def profile(request):
    return render(request, 'profile.html')
