from django.contrib import admin
from .models import question

# Register your models here.
@admin.register(question)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status',)
    search_fields = ('title', 'content',)
    list_filter = ('author',)
    prepopulated_fields = {'slug' : ('title',)}