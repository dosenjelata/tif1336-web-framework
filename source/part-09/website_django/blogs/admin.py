from django.contrib import admin
from .models import Post, ContactMessage

admin.site.register(Post)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    list_filter = ("created_at",)
