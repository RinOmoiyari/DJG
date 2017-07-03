from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^deliverables/$', views.deliverable_list, name='deliverable_list'),
    url(r'^deliverables_tasks/$', views.deliverable_list_tasks, name='deliverable_list_tasks'),
    url(r'^deliverables/(?P<pk>\d+)/$', views.deliverable_details, name='deliverable_details'),
    url(r'^deliverables/new$', views.deliverable_new, name='deliverable_new'),
    url(r'^deliverables/(?P<pk>\d+)/edit$', views.deliverable_edit, name='deliverable_edit'),
]
