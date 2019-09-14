from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SalaryModelForm, WorklogModelForm, TravelexModelForm
from .models import Salary, Worklog, Travelex





class UpdateViewMessageMixin(UpdateView):

    def form_valid(self, form):
        message = f'"{form.instance}" has been updated.'
        messages.success(self.request, message)
        return super().form_valid(form)





class SuccessURLMixin:
    success_url = reverse_lazy('mypage')





class SalaryModelMixin(LoginRequiredMixin):
    model = Salary

class SalaryFormMixin(SalaryModelMixin, SuccessURLMixin):
    form_class = SalaryModelForm






class TravelexModelMixin(LoginRequiredMixin):
    model = Travelex

class TravelexFormMixin(TravelexModelMixin, SuccessURLMixin):
    form_class = TravelexModelForm








class WorklogModelMixin(LoginRequiredMixin):
    model = Worklog

class WorklogFormMixin(WorklogModelMixin, SuccessURLMixin):
    form_class = WorklogModelForm