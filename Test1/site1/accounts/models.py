from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset()
		
class UserProfile(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	credit_card_number = models.CharField(max_length=100, default='')
	phone_number = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='profile_image', blank=True)
	
	USERNAME_FIELD = 'username'
	def __str__(self):
		return self.username.username

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(username=instance)
