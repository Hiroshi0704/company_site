from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Salary, Worklog, Travelex
from .forms import WorklogModelForm, TravelexModelForm



# MARK: - Home

class MyPageView(LoginRequiredMixin,TemplateView):
    template_name = 'atend/mypage.html'



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
    form_class = TravelexModelForm
    success_url = reverse_lazy('mypage')

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
    form_class = WorklogModelForm
    success_url = reverse_lazy('mypage')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        print(form)
        return super().form_valid(form)

class WorklogListView(LoginRequiredMixin,ListView):
    model = Worklog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklog_list'] = Worklog.objects.filter(staff=self.request.user)
        return context

