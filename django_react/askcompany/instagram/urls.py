from django.urls import path, re_path, register_converter

from . import views
from .converter import YearConverter


register_converter(YearConverter, 'year')

app_name = 'instagram'  # URL Reverse에서 namespace 역할을 하게 됨

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    # path('archives/<year:year>/', views.archives_year),
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
]