# service/urls.py
from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.activity_list, name='activity-list'),
    path('<int:activity_id>/', views.activity_detail, name='activity-detail'),
    path('<int:activity_id>/sign/', views.signup_view, name='activity-signup'),
    path('<int:activity_id>/comment/', views.comment_list, name='comment-list'),
    path('<int:activity_id>/comment/write/', views.comment_create, name='write-comment'),
]
