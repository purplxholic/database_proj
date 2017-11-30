from django.conf.urls import url

from . import views

app_name = 'browser'
urlpatterns = [
    url(r'^$', views.BrowseView.as_view(), name='index'),
    url(r'^results$', views.BrowseResultsView.as_view(), name='browse-results')
]