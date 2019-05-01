from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
from home.models import Friend
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = RegistrationForm()
		
	args = {'form': form}
	return render(request, 'accounts/reg_form.html', args)


def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user
	args = {'user': user}
	return render(request, 'accounts/profile.html', args)
	

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('view_profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('view_profile')
		else:
			return redirect('change_password')
	else:
		form = PasswordChangeForm(user=request.user)
		
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
		
def friend_list(request):
		friend = None
		friends = None
		if request.user.is_authenticated:
			friend, created = Friend.objects.get_or_create(current_user=request.user)
			friends = friend.users.all()
		args = {
			'friends': friends,
		}
		return render(request, 'accounts/friend_list.html', args)