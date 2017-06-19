from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_details, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/publish$', views.publish_post, name='publish'),
]
