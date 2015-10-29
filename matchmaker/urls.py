__author__ = 'philward'

from django.conf.urls import patterns, url
from matchmaker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_instrument/$', views.add_instrument, name='add_instrument')
)