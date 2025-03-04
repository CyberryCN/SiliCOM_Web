# polls/urls.py
from django.urls import path
from . import views

app_name = 'introduction'  # 命名空间（可选）

urlpatterns = [
    path('', views.index, name='index'),  # 根路径指向 社团简介 的首页
    # 其他路由...
]
