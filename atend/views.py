from django.urls import reverse, reverse_lazy
from django.contrib import messages
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
    fields = ['start_place', 'end_place', 'date', 'value', 'reason']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        return super().form_valid(form)


class TravelexListView(LoginRequiredMixin,ListView):
    model = Travelex

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['travelex_list'] = Travelex.objects.filter(staff=self.request.user)
        return context



# MARK: - Worklog

class WorklogCreateView(LoginRequiredMixin,CreateView):
    model = Worklog
    fields = ['date', 'file', 'comment']
    # fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        return super().form_valid(form)

class WorklogListView(LoginRequiredMixin,ListView):
    model = Worklog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklog_list'] = Worklog.objects.filter(staff=self.request.user)
        return context

