from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Subdivision(models.Model):
    subdivision_name = models.CharField(max_length=256, verbose_name='Название подразделения')

    def __str__(self):
        return self.subdivision_name


class Position(models.Model):
    position_name = models.CharField(max_length=256, verbose_name='Название должности')

    def __str__(self):
        return self.position_name


class Employee(models.Model):

    full_name = models.CharField(verbose_name='ФИО сотрудника', max_length=256)
    subdivision = models.ForeignKey(Subdivision, verbose_name='Подразделение', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, max_length=256, verbose_name='Должность', on_delete=models.CASCADE)
    started_work_date = models.DateField(verbose_name='Дата начала работы', default=timezone.now)
    experience = models.PositiveIntegerField(verbose_name='Стаж', default=0)



