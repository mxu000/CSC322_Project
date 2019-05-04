from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from home.forms import HomeForm
from home.models import Post, Friend, Friend_Request

class HomeView(TemplateView):
	template_name = 'home/home.html'
	
	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created_date', '-updated_date')
		args = {
			'form': form, 
			'posts': posts,
		}
		return render(request, self.template_name, args)
		
	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('home')
		args = {'form': form, 'text': text}
		return render(request, self.template_name, args)
		
def change_friends(request, operation, pk):		
	friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend_Request.create_reqs(request.user, friend)
	elif operation == 'remove':
		Friend.remove_friend(request.user, friend)
		Friend_Request.decline_request(request.user, friend)
	else:
		return redirect('home')
	return redirect('friend_list')

def friend_requests(request, operation, pk):
	friend = User.objects.get(pk=pk)
	if operation == 'accept':
		Friend_Request.accept_request(request.user, friend)
		Friend.add_friend(request.user, friend)
		Friend.add_friend(friend, request.user)
	elif operation == 'decline':
		Friend_Request.decline_request(request.user, friend)
	else:
		return redirect('home')
	return redirect('friend_list')
			