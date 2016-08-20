from django.conf.urls import url

from admins import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]