"""testdatagen URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from jsondata import views as json_views
from csvdata import views as csv_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # JSON DATA #
    url(r'^json/$', json_views.index),
    url(r'^json/generate$', json_views.generate),
    # CSV DATA #
    url(r'^csv/$', csv_views.index),
    url(r'^csv/generate$', csv_views.generate),
]
