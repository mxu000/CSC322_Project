from django.contrib import admin
from home.models import Post, Friend, Friend_Request

# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Friend_Request)