from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/(?P<pk>[0-9]+)/accept/$', views.task_accept, name='task_accept'),
    url(r'^task/(?P<pk>[0-9]+)/remove/$', views.task_remove, name='task_remove'),
]
