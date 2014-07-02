from django.conf.urls import patterns, include, url
from fashion import views

urlpatterns = patterns('',
	#Index
	url(r'^EyelessUser/$', views.eyeless_user, name='User'),
	url(r'^userView/(?P<EyelessUser_id>\d+)/$', views.userview, name='userView'),
)
