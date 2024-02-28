from django.contrib import admin

from commander import models

@admin.register(models.AdminCommanderLog)
class AdminCommanderLogAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "command",
        "created_at",
    )
    readonly_fields = "pk", "user", "command", "output", "created_at"
    search_fields = ("command",)
    list_filter = (
        "user",
        "created_at",
    )
    list_per_page = 20

    def has_delete_permission(self, request, obj=None):
        return False
