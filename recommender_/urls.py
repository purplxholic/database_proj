from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<sk>\d+)/$', views.RecommenderView.as_view())]


