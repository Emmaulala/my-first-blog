#這個檔案是我創的
from django.urls import path, re_path #regex需要用re_path
from . import views

urlpatterns=[
    #path(r'^$', views.post_list, name='post_list'), #原本path寫法用regex會有warning，應該是混用新舊版本django寫法
    re_path(r'^$', views.post_list, name='post_list') #要用re_path寫法搭配regex才行
]  