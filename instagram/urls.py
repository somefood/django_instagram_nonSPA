from django.urls import path, re_path, register_converter
from . import views


app_name = 'instagram'
urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]