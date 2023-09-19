from django.urls import re_path as url,include
# from django.conf.urls import url,include
from  . import views

app_name = 'web'
urlpatterns = [

    url(r'jiankong', views.jiankong, name='jiankong'),
    url(r'yuce', views.yuce, name='yuce'),
    url(r'yujing', views.yujing, name='yujing'),
    url(r'chakan', views.chakan, name='chakan'),
]