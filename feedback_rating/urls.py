from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', views.music_info, name='music_info'),
	url(r'^$', views.index, name='index')
]
