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


class Salary(models.Model):

    date    = models.DateField()
    file    = models.FileField(upload_to='salary/%Y/%m/%d/', verbose_name='添付ファイル')
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff}: {self.file.name}'

class Worklog(models.Model):

    date    = models.DateField()
    file    = models.FileField(upload_to='worklog/%Y/%m/%d/', verbose_name='添付ファイル')
    comment = models.CharField(max_length=255)
    staff   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff}: {self.file.name}'