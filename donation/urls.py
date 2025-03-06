from django.urls import path
from . import  views

app_name = 'donation'

urlpatterns = [
    path('', views.donor_list, name='donor_list'),
]