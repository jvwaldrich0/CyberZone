from django.contrib import admin
from .models import post

# Register your models here.
@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at', 'author')
    date_hierarchy = ('published_at')
    prepopulated_fields = {'slug' : ('title',)}