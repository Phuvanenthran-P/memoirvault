from django.contrib import admin
from .models import Moment


@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at")
    list_filter = ("created_at", "remind_me")
    search_fields = ("title", "owner__username")
