from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'message',
        "message_length",
        'created_at',
        'updated_at',
        "is_public",
    ]
    list_display_links = ['message']
    search_fields = ["message"]
    list_filter = ['is_public']
