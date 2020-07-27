from django.urls import path
from . import views

app_name = 'blog1'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
]