from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.User_Record_View.as_view())]


