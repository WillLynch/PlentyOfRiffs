__author__ = 'philward'

from django.conf.urls import patterns, url
from matchmaker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_instrument/$', views.add_instrument, name='add_instrument'),
        url(r'^profile/$', views.profile, name="profile"),
        url(r'^edit_personal_info/$', views.edit_personal_info, name="edit_personal_info"),
        url(r'^matches/$', views.matches, name="matches"),
        url(r'^add_genre/$', views.add_genre, name="add_genre")
)