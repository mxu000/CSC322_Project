from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile

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
			
		def save(self, commit=True):
			UserProfile = super(UserCreationForm, self).save(commit=False)
			UserProfile.username = self.cleaned_data['username']
			UserProfile.first_name = self.cleaned_data['first_name']
			UserProfile.last_name = self.cleaned_data['last_name']
			UserProfile.email = self.cleaned_data['email']
			UserProfile.address = self.cleaned_data['address']
			UserProfile.credit_card_number = self.cleaned_data['credit_card_number']
			UserProfile.phone_number = self.cleaned_data['phone_number']
			if commit:
				UserProfile.save()
			
			return UserProfile
			
class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = User
		fields = (
		'first_name',
		'last_name',
		'email',
		'password',
		)
		