from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import signupForm, signinForm, makeprojectForm
from .models import Signup


def firstpg_func(request):
    return  render(request, 'firstpg.html')


def signup_func(request):
    form = signupForm()
    if request.method == 'POST':
        username2 = request.POST["username"]
        try:
            Signup.objects.get(username = username2)
            return render (request, 'signup.html', {'error':'このユーザー名は既に登録されています'})
        except:
            Signup.objects.create_user(username = username2)
            return render (request, 'signup.html')
    if request.method == 'POST':
        form = signupForm(request.POST) #requestがPOSTならformにrequestのPOST情報を入れる
        if form.is_valid():             #formの内容に誤りがなければ内容を保存する
            form.save(commit=True)
            return redirect('profile')    
        else:
            print('入力に誤りがあります')
    return render (request, 'signup.html', {'form':form}) #keyのformがsignup.htmlにあったらsignupFormが入る


def signin_func(request):
    form = signinForm()
    return render (request, 'signin.html', {'form':form}) #keyのformがsignin.htmlにあったらsigninFormが入る

def makeproject_func(request):
    form = makeprojectForm
    return render(request, 'makeproject.html', {'form':form})


def profile_func(request):
    return render(request, 'profile.html')
