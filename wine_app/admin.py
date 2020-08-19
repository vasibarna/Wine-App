from django.contrib import admin
from .models import Wine, Category, PostImage, UserProfile

admin.site.register(Wine)
admin.site.register(Category)
admin.site.register(PostImage)
admin.site.register(UserProfile)
