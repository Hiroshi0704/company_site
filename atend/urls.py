from django.urls import path

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('atend/salary/list/', SalaryListView.as_view(), name='salary_list'),
    path('atend/travelex/create/', TravelexCreateView.as_view(), name='travelex_create'),
    path('atend/travelex/list/', TravelexListView.as_view(), name='travelex_list'),
    path('atend/worklog/create/', WorklogCreateView.as_view(), name='worklog_create'),
]