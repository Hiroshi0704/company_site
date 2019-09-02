from django.db import models


class Travelex(models.Model):

    date  = models.DateField()
    start_place = models.CharField(max_length=255)
    end_place   = models.CharField(max_length=255)
    value  = models.IntegerField()
    reason = models.CharField(max_length=255)

    def __str__(self):
        return  self.date + '' + self.start_place + '~' + self.end_place + ': ' + self.value


class Salary(models.Model):

    date = models.DateField()
    file = models.FileField()