from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile
from home.models import Post

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)

			
class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = User
		fields = (
		'first_name',
		'last_name',
		'email',
		'password',
		)

class SearchUser(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': '...',
			}
		))
	
	class Meta:
		model = Post
		fields = (
			'post',
			
		)
