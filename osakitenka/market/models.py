from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

class item(models.Model):
	CATEGORIES = (
			('GEN', 'GENERAL'),
			('CLO', 'CLOTHES'),
			('ELE', 'ELECTRONICS'),
	)
	title = models.CharField(max_length = 255)
	price = models.DecimalField(max_digits = 8, decimal_places = 2)
	image = models.ImageField(upload_to = 'item_images', default = 'default.png', blank = 'true')
	quantity = models.IntegerField(default = 0)
	description = models.CharField(max_length = 500)
	category = models.CharField(max_length = 3, choices = CATEGORIES, default = 'GEN')

	def __str__(self):
		return 'ID:' + str(self.pk) + ' ' + self.title

class listing(models.Model):
	seller = models.ForeignKey(User, on_delete = models.CASCADE)
	product_id = models.ForeignKey(item, on_delete = models.CASCADE)
	number_of_bids = models.IntegerField(default = 0)
	time_starting = models.DateTimeField(default = datetime.now, blank = True)
	time_ending = models.DateTimeField()

	def __str__(self):
		return 'ID:' + str(self.pk) + ' PRODUCT_ID:' + str(self.product_id) + ' SELLER:' + str(self.seller)


