from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^unpublished$', views.post_unpublished, name='post_unpublished'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/publish$', views.post_publish, name='post_publish'),
        url(r'^post/(?P<pk>\d+)/delete$', views.post_delete, name='post_delete'),
    url(r'^post/new$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit$', views.post_edit, name='post_edit'),
]
