from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	address = forms.CharField(required=True)
	credit_card_number = forms.CharField(required=True)
	phone_number = forms.CharField(required=True)
	class Meta:
		model = UserProfile
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'address',
			'credit_card_number',
			'phone_number',
			'password1',
			'password2',
			)
			
		def save(self, commit=True):
			userprofile = super(RegistrationForm, self).save(commit=False)
			userprofile.first_name = self.cleaned_data['first_name']
			userprofile.last_name = self.cleaned_data['last_name']
			userprofile.email = self.cleaned_data['email']
			userprofile.address = self.cleaned_data['address']
			userprofile.credit_card_number = self.cleaned_data['credit_card_number']
			userprofile.phone_number = self.cleaned_data['phone_number']
			
			if commit:
				userprofile.save()
			
			return userprofile
			
class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = UserProfile
		fields = (
		'first_name',
		'last_name',
		'email',	
		'address',
		'credit_card_number',
		'phone_number',
		'image',
		'password',
		)
		