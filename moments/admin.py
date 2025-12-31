from django.contrib import admin
from .models import Moment

@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "memory_date",
        "is_annual",
        "created_at",
    )

    list_filter = (
        "is_annual",
        "memory_date",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = ("-created_at",)
