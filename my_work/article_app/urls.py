from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('',views.article_list,name='list'),
    path('write/',views.write,name='write'),
    path('article/', views.article, name='article'),
    path('<int:article_id>/',views.real_article,name='real_article'),
]