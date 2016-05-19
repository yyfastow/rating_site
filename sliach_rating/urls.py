from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sluchim_list, name='list'),
    url(r'search/$', views.search_state, name='search'),
    url(r'(?P<pk>\d+)/$', views.sliach_details, name='details')
]

