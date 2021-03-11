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

class SetPlan(models.Model):
    MINUTES = (
        ('','minutes'),
        ('1',15),
        ('2',25),
        ('3',50),
    )
    SETS = (
        ('','sets'),
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
        ('6',6),
        ('7',7),
        ('8',8),
        ('9',9),
        ('10',10),
    )

    minute = models.CharField('分', choices=MINUTES, max_length=200, blank=False, default='0')
    sets = models.CharField('セット回数', choices=SETS, max_length=200, blank=False, default='0')
    total = models.CharField('総勉強時間', max_length=200, blank=False, default='0')
    SelfAssesment = models.TextField('自己評価', blank=False)
    Comment = models.TextField('コメント', blank=False)