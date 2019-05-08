import re

from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		response = self.get_response(request)
		return response
		
	def process_view(self, request, view_func, view_args, view_kwargs):
		assert hasattr(request, 'user')
		path = request.path_info
		url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
		if path == '/home/':
			return request.GET.get(settings.LOGIN_REDIRECT_URL)

		elif request.user.is_authenticated and url_is_exempt:
			print("1")
			return redirect(settings.LOGIN_REDIRECT_URL)
			
		elif request.user.is_authenticated or url_is_exempt:
			print("2")
			return None
		
		elif not request.user.is_authenticated or not url_is_exempt:
			print("3")
			return redirect(settings.LOGIN_URL)
		else:
			print("4")
			return request.GET.get(path)
			