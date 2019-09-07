# Generated by Django 2.2 on 2019-09-07 07:01

import atend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='file',
            field=models.FileField(upload_to=atend.models.salary_path),
        ),
        migrations.AlterField(
            model_name='travelex',
            name='reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='worklog',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='worklog',
            name='file',
            field=models.FileField(upload_to=atend.models.worklog_path),
        ),
    ]
