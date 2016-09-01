from django.conf.urls import url

from admins import views

urlpatterns = [
	url(r'^admin_login/$', views.admin_login, name='admin_login'),
	url(r'^admin_logout/$', views.admin_logout, name='admin_logout'),
	url(r'^admin_page/$', views.admin_page, name='admin_page'),
	url(r'^society_details/$', views.society_details, name='society_details')
]