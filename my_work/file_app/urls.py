from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin

app_name = 'file'

urlpatterns = [
    # path('upload/',views.upload,name='upload'),
    # path('search',views.search,name='search'),
    # path('download/',views.download,name='download'),
    path('success/',views.success,name='success'),
    path('local_upload/',views.local_upload,name='local_upload'),
    #可视化文件上传
    path('', views.HomeView.as_view(), name='index'),
    url(r'^s/(?P<code>\d+)/$', views.DisplayView.as_view()),
    path('my/',views.MyView.as_view(), name="my"),
    path('search/', views.SearchView.as_view(), name="search"),
]