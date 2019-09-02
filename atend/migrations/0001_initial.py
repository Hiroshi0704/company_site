# Generated by Django 2.2 on 2019-09-02 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Travelex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_place', models.CharField(max_length=255)),
                ('end_place', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
                ('reason', models.CharField(max_length=255)),
            ],
        ),
    ]
