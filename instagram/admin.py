from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "photo_tag",
        'message',
        "message_length",
        'created_at',
        'updated_at',
        "is_public",
    ]
    list_display_links = ['message']
    search_fields = ["message"]
    list_filter = ['is_public']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:100px;"/>')
        return None
