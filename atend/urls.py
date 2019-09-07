from django.urls import path

from .views import (
    MyPageView, 
    SalaryListView, 
    TravelexCreateView, TravelexListView, 
    WorklogCreateView, WorklogListView,
)

urlpatterns = [
    path('', MyPageView.as_view(), name='mypage'),
    path('salary/list/', SalaryListView.as_view(), name='salary_list'),

    path('travelex/create/', TravelexCreateView.as_view(), name='travelex_create'),
    path('travelex/list/', TravelexListView.as_view(), name='travelex_list'),
    
    path('worklog/create/', WorklogCreateView.as_view(), name='worklog_create'),
    path('worklog/list/', WorklogListView.as_view(), name='worklog_list'),
]