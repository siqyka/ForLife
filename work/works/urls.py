from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', work_views,name='work'),
]
