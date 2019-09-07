from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Salary, Worklog, Travelex



# MARK: - Home

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'atend/home.html'



# MARK: - Salary

class SalaryListView(LoginRequiredMixin,ListView):
    model = Salary

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salary_list'] = Salary.objects.filter(staff=self.request.user)
        return context



# MARK: - Traveling Expenses

class TravelexCreateView(LoginRequiredMixin,CreateView):
    model = Travelex
    fields = '__all__'

class TravelexListView(LoginRequiredMixin,ListView):
    model = Travelex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['travelex_list'] = Travelex.objects.filter(staff=self.request.user)
        return context



# MARK: - Worklog

class WorklogCreateView(LoginRequiredMixin,CreateView):
    model = Worklog
    fields = '__all__'

class WorklogListView(LoginRequiredMixin,ListView):
    model = Worklog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklog_list'] = Worklog.objects.filter(staff=self.request.user)
        return context

