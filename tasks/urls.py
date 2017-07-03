from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^tasks/(?P<pk>\d+)/$', views.task_details, name='task_details'),
    url(r'^tasks/new$', views.task_new, name='task_new'),
    url(r'^tasks/new/deliv_id=(?P<deliv_id>\d+)$', views.task_new, name='task_new_from_deliv'),
    url(r'^tasks/(?P<pk>\d+)/edit$', views.task_edit, name='task_edit'),
]
