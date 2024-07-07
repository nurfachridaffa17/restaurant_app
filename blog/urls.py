from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.potst_list, name='potst_list'),
    path('tag/<slug:tag>/', views.post_by_tag, name='post_by_tag'),
    path('category=<slug:category>/', views.post_by_category, name='post_by_category'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]