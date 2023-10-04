from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_filter = ['name','price']
    search_fields = ['name','price']
    
admin.site.register(Post,PostAdmin)
    