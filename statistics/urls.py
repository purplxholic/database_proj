from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stats_choice/(?P<choice>[a-z]+)/(?P<top_no>[0-9]+)$', views.stats_choice, name='stats_choice')
]
