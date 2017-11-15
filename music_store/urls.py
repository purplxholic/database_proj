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
<<<<<<< HEAD
from django.conf.urls import url, include
=======
from django.conf.urls import url, include
>>>>>>> zanette
=======
from django.conf.urls import url, include
>>>>>>> 51f8161da0e9cec57b26ab446f53d1d6db38e1a3
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^music/', include('feedback_rating.urls')),
=======
    url(r'^statistics/', include('statistics.urls')),
    url(r'^inventory/', include('inventory_system.urls')) #shortened url for user ease
>>>>>>> zanette
=======
    url(r'^music/', include('feedback_rating.urls'))
>>>>>>> 51f8161da0e9cec57b26ab446f53d1d6db38e1a3
]
