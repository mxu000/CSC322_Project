from django.urls import path
from django.conf.urls import url
from home.views import HomeView
from . import views

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friend'),
]