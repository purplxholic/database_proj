from django.conf.urls import url
from . import views

app_name = 'Recommender'
urlpatterns = [
    url(r'^',views.RecommenderView.as_view())
]
# TODO Say hi to Tenzin

