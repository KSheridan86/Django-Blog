from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Docstrings are us!!!
    """
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Docstrings are us!!!
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Docstrings are us!!!
        """
        queryset.update(approved=True)
