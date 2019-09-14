from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Salary, Worklog, Travelex
from .forms import SalaryModelForm, WorklogModelForm, TravelexModelForm
from .mixins import (
    SalaryModelMixin, SalaryFormMixin, 
    TravelexFormMixin, TravelexModelMixin, WorklogFormMixin, WorklogModelMixin
)


class UpdateViewMessageMixin(UpdateView):

    def form_valid(self, form):
        message = f'"{form.instance}" has been updated.'
        messages.success(self.request, message)
        return super().form_valid(form)




# MARK: - My Page ------------------------------------------

class MyPageView(LoginRequiredMixin,TemplateView):
    template_name = 'atend/mypage.html'




# MARK: - Salary ------------------------------------------

class SalaryListView(SalaryModelMixin, ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salary_list'] = Salary.objects.filter(staff=self.request.user)
        return context

class SalaryCreateView(SalaryFormMixin, CreateView):
    
    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        return super().form_valid(form)

class SalaryUpdateView(SalaryFormMixin, UpdateViewMessageMixin):
    pass





# MARK: - Traveling Expenses ------------------------------------------

class TravelexCreateView(TravelexFormMixin,CreateView):



    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        return super().form_valid(form)


class TravelexListView(TravelexModelMixin,ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['travelex_list'] = Travelex.objects.filter(staff=self.request.user)
        return context




class TravelexUpdateView(TravelexFormMixin,UpdateViewMessageMixin):
    pass



# MARK: - Worklog ------------------------------------------

class WorklogCreateView(WorklogFormMixin,CreateView):
    
    def form_valid(self, form):
        form.instance.staff = self.request.user
        message = f'"{form.instance}" has been requested.'
        messages.info(self.request, message)
        print(form)
        return super().form_valid(form)

class WorklogUpdateView(WorklogFormMixin,UpdateViewMessageMixin):
    pass

class WorklogListView(WorklogModelMixin,ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worklog_list'] = Worklog.objects.filter(staff=self.request.user)
        return context
