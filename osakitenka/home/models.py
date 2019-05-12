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

############## NEW #################################################
class Product(models.Model):
	CATEGORIES = (
		('LAP', 'Laptop'),
		('CON', 'Console'),
		('GAD', 'Gadget'),
		('GAM', 'Game'),
		('TEL', 'TV')
	)
	
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='images/')
	description = models.CharField(max_length=500)
	quantity = models.IntegerField()
	category = models.CharField(
		max_length=2,
		choices=CATEGORIES
	)
	date_posted = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "ID:" + str(self.pk) + " " + self.title

class Auction(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
	number_of_bids = models.IntegerField()
	time_starting = models.DateTimeField()
	time_ending = models.DateTimeField()
	
	def __str__(self):
		return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)

class Watchlist(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)

class Bid(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	bid_time = models.DateTimeField()
	
	def __str__(self):
		return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + \
			str(self.auction_id) + " " + str(self.bid_time) 

class Chat(models.Model):
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()
	time_sent = models.DateTimeField()

	def __str__(self):
		return "AUCTION_ID:" + str(self.auction_id) + " USER_ID:" + str(self.user_id)