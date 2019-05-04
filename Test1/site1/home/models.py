from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	post = models.CharField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	
class Friend(models.Model):
	users = models.ManyToManyField(User, blank=True)
	current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
	
	@classmethod
	def add_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user = current_user
		)
		friend.users.add(new_friend)
		
	@classmethod
	def remove_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user = current_user
		)
		friend.users.remove(new_friend)

class Friend_Request(models.Model):
	current_user = models.ForeignKey(User, related_name='sender', null=True, on_delete=models.SET_NULL)
	request_user = models.ForeignKey(User, related_name='receive', null=True, on_delete=models.SET_NULL)
	is_approved = models.BooleanField(default=False)

	@classmethod
	def create_reqs(cls, current_user, new_friend):
		friend0, created = cls.objects.get_or_create(
			current_user = current_user,
			request_user = new_friend
			)

	@classmethod
	def accept_request(cls, current_user, new_friend):
		friend0, created = cls.objects.get_or_create(
			current_user = current_user,
			request_user = new_friend
			)
		friend1, created = cls.objects.get_or_create(
			request_user = current_user,
			current_user = new_friend
			)
		friend0.is_approved = True
		friend1.is_approved = True
		friend0.save()
		friend1.save()

	@classmethod
	def decline_request(cls, current_user, new_friend):
		friend0, created = cls.objects.get_or_create(
			current_user = current_user,
			request_user = new_friend
			)
		friend1, created = cls.objects.get_or_create(
			request_user = current_user,
			current_user = new_friend
			)
		friend0.delete()
		friend1.delete()