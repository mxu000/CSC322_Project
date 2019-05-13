from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from home.forms import HomeForm
from home.models import Post, Friend

class HomeView(TemplateView):
	template_name = 'home/home.html'
	
	def get(self, request):
		form = HomeForm()
		posts = Post.objects.all().order_by('-created_date', '-updated_date')
		users1 = User.objects.exclude(id = request.user.id)
		users = users1.exclude(id = 1)
		friend = None
		friends = None
		if request.user.is_authenticated:
			friend, created = Friend.objects.get_or_create(current_user=request.user)
			friends = friend.users.all()
		args = {
			'form': form, 
			'posts': posts, 
			'users': users, 
			'friends': friends,
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
		Friend.add_friend(request.user, friend)
	elif operation == 'remove':
		Friend.remove_friend(request.user, friend)
	else:
		return redirect('home')
	return redirect('friend_list')
			