from django.conf import settings
from django.db import models
from django.utils import timezone


class Signup(models.Model):
    username = models.CharField('ユーザー名', max_length = 200)
    password = models.CharField('パスワード', max_length = 200)
    def __str__(self):
        return self.username
    

class Signin(models.Model):
    username = models.CharField('ユーザー名', max_length = 200)
    password = models.CharField('パスワード', max_length = 200)
    def __str__(self):
        return self.username


class Project(models.Model):
    project_name = models.CharField('プロジェクト名', max_length=200)
    due_date = models.DateField('試験日', blank=False)
    description = models.TextField('目標概要', blank=False)
    def __str__(self):
        return self.project_name