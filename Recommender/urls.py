from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^',views.BrowseResultsView.as_view())
]