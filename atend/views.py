from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .models import Salary, Worklog, Travelex

class HomePageView(TemplateView):
    template_name = 'atend/home.html'


class SalaryListView(ListView):
    model = Salary

class TravelexCreateView(CreateView):
    model = Travelex
    fields = '__all__'

