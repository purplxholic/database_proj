"""music_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', include('signup.urls')),
    url(r'^home/$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('feedback_rating.urls')),
    url(r'^statistics/', include('statistics.urls')),
    url(r'^inventory/', include('inventory_system.urls')), #shortened url for user ease
    url(r'^browse/', include('browser.urls')),
    url(r'^Recommender/', include('recommender_.urls')),
    url(r'^myrecord/', include('user_record.urls')),
    url(r'^order/', include('order.urls'))
]
