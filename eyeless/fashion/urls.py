from django.conf.urls import patterns, include, url
from fashion import views

urlpatterns = patterns('',
	#Index
	url(r'^EyelessUser/$', views.eyeless_user, name='User'),
	url(r'^userView/(?P<EyelessUser_id>\d+)/$', views.userview, name='userView'),
	url(r'^EyelessStylist/$', views.eyeless_stylist, name='Style'),
	url(r'^styleView/(?P<EyelessStylist_id>\d+)/$', views.styleview, name='styleView'),
)
