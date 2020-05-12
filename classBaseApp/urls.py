from django.urls import path
from classBaseApp.views import MyView, CustomerView, CustomerListView

app_name = 'classBaseApp'

urlpatterns = [
    path('', MyView.as_view()),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('customer/list', CustomerListView.as_view()),
]