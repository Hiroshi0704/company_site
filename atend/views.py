from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import Salary, Worklog, Travelex



# MARK: - Home

class HomePageView(TemplateView):
    template_name = 'atend/home.html'



# MARK: - Salary

class SalaryListView(ListView):
    model = Salary



# MARK: - Traveling Expenses

class TravelexCreateView(CreateView):
    model = Travelex
    fields = '__all__'

class TravelexListView(ListView):
    model = Travelex



# MARK: - Worklog

class WorklogCreateView(CreateView):
    model = Worklog
    fields = '__all__'

