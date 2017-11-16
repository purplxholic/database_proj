from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^moreLicense/(?P<sid>[0-9]{10})/(?P<more_amt>[0-9]+)$', views.moreLicense, name='moreLicense'),
    #sid,name,aid,gid,releaseDate,numDownloads,numLicense
    #this url is so bad and long w/ sos many regex that I think this needs to refine and multiple testss
    url(r'^newMusic/(?P<sid>[0-9]{10})/(?P<name>[A-Za-z]+)/(?P<aid>[0-9]{10})/(?P<gid>[0-9]{10})/(?P<releaseDate>\d{4}[-/]\d{2}[-/]\d{2})/(?P<numDownloads>[0]{1})/(?P<numLicense>[0-9]+)$', views.newMusic, name='newMusic')
]
