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
    reason  = models.CharField(max_length=255, blank=True, null=True)
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Staff Name: {self.staff}, Date: {self.date}, {self.start_place} ~ {self.end_place}: {self.value}'



def salary_path(instance, filename):
    return f'salary/{instance.staff.username}/{instance.date.strftime("%Y/%m")}/{filename}'

class Salary(models.Model):

    date    = models.DateField()
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file    = models.FileField(upload_to=salary_path)

    def __str__(self):
        return f'{self.staff} {self.date} {self.get_file_name()}'

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_strftime(self):
        return self.date.strftime('%Y/%m')

    def get_download_name(self):
        return f'{self.staff}_{self.get_file_name()}'



def worklog_path(instance, filename):
    return f'worklog/{instance.staff.username}/{instance.date.strftime("%Y/%m")}/{filename}'

class Worklog(models.Model):

    date    = models.DateField()
    file    = models.FileField(upload_to=worklog_path)
    comment = models.CharField(max_length=255, blank=True, null=True)
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff}: {self.file.name}'

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_download_name(self):
        return f'{self.staff}_{self.get_file_name()}'