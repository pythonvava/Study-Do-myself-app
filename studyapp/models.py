from django.conf import settings
from django.db import models
from django.utils import timezone


class Project(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField('プロジェクト名', max_length=200, blank=False)
    description = models.TextField('目標', blank=False)
    expenses_item = models.CharField('経費項目', max_length=200, blank=True)
    expenses = models.CharField('経費', max_length=200, blank=True)
    build_date = models.DateField(verbose_name='作成日', blank=True, default=timezone.datetime.today())
    due_date = models.DateField(verbose_name='設定日', blank=True, null=True)

    def __str__(self):
        return self.project_name


class StudyDetail(models.Model):
    StudyDate = models.DateField('勉強日', blank=False)
    StudyTime = models.DateField('勉強時間', blank=False)
    SelfAssesment = models.TextField('自己評価', blank=False)
    Comment = models.TextField('コメント', blank=False)

