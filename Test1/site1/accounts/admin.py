from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'email')
	
	def first_name(self, obj):
		return obj.first_name
	
	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('username')
		return queryset
	
admin.site.register(UserProfile, UserProfileAdmin)