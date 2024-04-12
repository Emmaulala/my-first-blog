#這個檔案是我創的
from django.urls import path, re_path #regex需要用re_path
from . import views

urlpatterns=[
    #path(r'^$', views.post_list, name='post_list'), #原本path寫法用regex會有warning，應該是混用新舊版本django寫法
    re_path(r'^$', views.post_list, name='post_list'), #要用re_path寫法搭配regex才行
    re_path(r'^psot/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'), #注意不要加錯檔案到mysite.urls 會找不到add_comment_to_post funtion
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),


]  