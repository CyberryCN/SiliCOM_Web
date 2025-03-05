from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'sug'  # 命名空间（可选）

urlpatterns = [
    path('', views.level_list, name='level-list'),
    path('<int:level_id>/', views.book_list, name='book-list'),
    path('<int:level_id>/<slug:book_label>/',
         views.book_detail, name='book-detail'),
]