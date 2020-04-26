from django.urls import path
from classBaseApp.views import MyView, CustomerView

app_name = 'classBaseApp'

urlpatterns = [
    path('', MyView.as_view()),
    path('customer/', CustomerView.as_view(), name='customer'),
]