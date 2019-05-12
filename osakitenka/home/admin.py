from django.contrib import admin
from home.models import Post, Friend, Product, Auction, Chat, Watchlist, Bid

# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)

admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)

