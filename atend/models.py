import os
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

class Travelex(models.Model):

    start_place = models.CharField(max_length=255)
    end_place   = models.CharField(max_length=255)
    date    = models.DateField()
    value   = models.IntegerField()
    reason  = models.CharField(max_length=255)
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff} {self.date} {self.start_place} ~ {self.end_place}: {self.value}'






def get_salary_path(instance, filename):
    return f'salary/{instance.staff.username}/{instance.date.strftime("%Y/%m")}/{filename}'

class Salary(models.Model):

    date    = models.DateField()
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file    = models.FileField(upload_to=get_salary_path, verbose_name='添付ファイル')

    def __str__(self):
        return f'{self.get_staff_username()} {self.get_strftime()} {self.get_file_name()}'

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_strftime(self):
        return self.date.strftime('%Y/%m')

    def get_staff_username(self):
        return self.staff.username

    def get_download_name(self):
        return f'{self.get_staff_username()}_{self.get_strftime()}_{self.get_file_name()}'



def get_worklog_path(instance, filename):
    return f'salary/{instance.staff.username}/{instance.date.strftime("%Y/%m")}/{filename}'

class Worklog(models.Model):

    date    = models.DateField()
    file    = models.FileField(upload_to=get_worklog_path, verbose_name='添付ファイル')
    comment = models.CharField(max_length=255)
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff}: {self.file.name}'