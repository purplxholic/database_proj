from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.RecommenderView.as_view())]


