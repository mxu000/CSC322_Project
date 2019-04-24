from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	credit_card_number = models.CharField(max_length=100, default='')
	phone_number = models.CharField(max_length=100, default='')
	
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)