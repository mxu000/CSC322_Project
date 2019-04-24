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
		model = User
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
			user = super(RegistrationForm, self).save(commit=False)
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
			user.email = self.cleaned_data['email']
			user.address = self.cleaned_data['address']
			user.credit_card_number = self.cleaned_data['credit_card_number']
			user.phone_number = self.cleaned_data['phone_number']
			
			if commit:
				user.save()
			
			return user
			
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
		'password',
		)