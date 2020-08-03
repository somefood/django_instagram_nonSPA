from django.contrib import admin
from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author']
    list_display_links = ['pk', 'author']
    search_fields = ['caption']


@admin.register(Tag)
class CommentAdmin(admin.ModelAdmin):
    pass