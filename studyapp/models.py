from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    project_name = models.CharField('プロジェクト名', max_length=200)
    description = models.TextField('目標概要', blank=False)
    def __str__(self):
        return self.project_name