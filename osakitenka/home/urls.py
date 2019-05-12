from django.urls import path
from django.conf.urls import url
from home.views import HomeView
from . import views

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friend'),

	path('category/<str:category>/', views.filter_auctions, name='filter_auctions'),
    path('watchlist/<int:auction_id>/', views.watchlist, name='watchlist'),
    path('balance/', views.balance, name='balance'),
    path('balance/topup/', views.topup, name='topup'),
    path('watchlist/', views.watchlist_page, name='watchlist'),
    path('bid/<int:auction_id>/', views.bid_page, name='bid_page'),
    path('bid/<int:auction_id>/comment/', views.comment, name='comment'),
    path('bid/<int:auction_id>/raise_bid/', views.raise_bid, name='raise_bid'),
]