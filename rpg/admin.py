from django.conf import settings
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from rpg import models


@admin.register(models.CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    # columns in the list view
    list_display = (
        "pk",
        "name",
        "description",
        "active_characters",
    )
    # fields non-present in the model definition must be declared as readonly
    readonly_fields = ("active_characters",)
    # enable ordering by particular fields
    ordering = ("name",)

    # read_only fields can be defined by a custom method named as the field
    def active_characters(self, obj):
        return obj.characters.count()

    # override queryset by annotating custom field, which objects can be ordered by
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(active_characters_count=Count("characters"))

    # enable ordering by a custom field
    active_characters.admin_order_field = "active_characters_count"


@admin.register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "banner_preview",
        "members",
    )
    readonly_fields = (
        "banner_preview",
        "members",
    )
    ordering = ("name",)

    # creating a html element with use of format_html
    def banner_preview(self, obj):
        base_width, base_height = "150px", "300px"
        large_width, large_height = "200px", "400px"

        style = f"""
            width: {base_width}; height: {base_height};
            transition: all 0.3s ease;
        """
        mouse_over_style = f"""
            this.style.width='{large_width}';
            this.style.height='{large_height}';
        """
        mouse_out_style = f"""
            this.style.width='{base_width}';
            this.style.height='{base_height}';
        """
        img = f"""
            <img 
                src='{settings.MEDIA_URL}{obj.banner.name}' 
                style='{style}' 
                onmouseover="{mouse_over_style}" 
                onmouseout="{mouse_out_style}" 
            />
        """
        return format_html(img)

    def members(self, obj):
        return obj.characters.count()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(members_count=Count("characters"))

    members.admin_order_field = "members_count"


@admin.register(models.Rarity)
class RarityAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "grade",
        "color",
    )
    # enable editing queryset in the list view
    list_editable = (
        "name",
        "grade",
        "color",
    )
    ordering = ("grade",)


@admin.register(models.Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    # enable searchbar with title field lookup
    search_fields = ("title",)
    # enable pagination
    list_per_page = 10


@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "guild",
        "healthbar",
    )
    list_filter = ("guild",)

    def healthbar(self, obj):
        hp_percent = obj.statistics.health / obj.statistics.max_health

        return hp_percent


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
