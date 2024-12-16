from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists body, post and approved fields for display in admin
    """
    list_display = ('body', 'post', 'approved',)
