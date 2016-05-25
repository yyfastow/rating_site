from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sluchim_list, name='list'),
    url(r'(?P<sliach_pk>\d+)/add comment/$', views.rating_create, name='create_rate'),
    url(r'search/$', views.search_state, name='search'),
    url(r'state/(?P<pk>\d+)/$', views.get_state, name='get'),
    url(r'(?P<pk>\d+)/$', views.sliach_details, name='details'),
]

