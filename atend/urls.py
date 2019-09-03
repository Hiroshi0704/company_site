from django.urls import path

from .views import (
    HomePageView, 
    SalaryListView, 
    TravelexCreateView, TravelexListView, 
    WorklogCreateView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('salary/list/', SalaryListView.as_view(), name='salary_list'),
    path('travelex/create/', TravelexCreateView.as_view(), name='travelex_create'),
    path('travelex/list/', TravelexListView.as_view(), name='travelex_list'),
    path('worklog/create/', WorklogCreateView.as_view(), name='worklog_create'),
]