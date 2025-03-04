from django.urls import path
from . import views

app_name = 'sug'  # 命名空间（可选）

urlpatterns = [
    path('', views.index, name='sug'),  # 根路径指向 购机指南 的首页
    # 其他路由...
]