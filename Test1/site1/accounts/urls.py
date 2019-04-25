from django.urls import path
from . import views
from django.contrib.auth.views import (
	LoginView, 
	LogoutView, 
	PasswordResetView, 
	PasswordResetDoneView, 
	PasswordResetConfirmView,
	PasswordResetCompleteView,
	)

urlpatterns = [
	path('', views.home),
	path('login/', LoginView.as_view(template_name= 'accounts/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name= 'accounts/logout.html'), name='logout'),
	path('register/', views.register, name='register'),
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change-password/', views.change_password, name='change_password'),
	path('reset-password/', 
		PasswordResetView.as_view(template_name= 'accounts/reset_password.html'), name='reset_password'),
	path('reset-password/done/', 
		PasswordResetDoneView.as_view(template_name= 'accounts/reset_password_done.html'), name='password_reset_done'),
	path('reset-password/confirm/<uidb64>/<token>/', 
		PasswordResetConfirmView.as_view(template_name= 'accounts/reset_password_confirm.html'), name='password_reset_confirm'),
	path('reset-password/complete/', 
		PasswordResetCompleteView.as_view(template_name= 'accounts/reset_password_confirm.html'), name='password_reset_complete'),
	path('reset-password/confirm/NA/set-password/', 
		PasswordResetConfirmView.as_view(template_name= 'accounts/reset_password_confirm.html'), name='set_password'),
	
]