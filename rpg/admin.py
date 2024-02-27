from django.conf import settings
from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
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
        "character_class",
        "level",
        "guild",
        "health",
        "mana",
        "exp",
        "gold_",  # underscore used to prevent field name collision
    )
    list_filter = ("guild",)

    def resource_bar(self, **kwargs):
        width = 100
        resource = getattr(kwargs["obj"], kwargs["resource"])
        resource_max = getattr(kwargs["obj"], f"max_{kwargs['resource']}")
        percent_width = int(resource / resource_max * width)

        out_bar_style = f"""
            border-radius: 5px;
            width: {width}px;
            height: 10px;
            background-color: #CCCCCC;
            padding: 2px;
        """
        in_bar_style = f"""
            border-radius: 5px;
            width: {percent_width}px;
            height: 10px;
            background-color: {kwargs["color"]};
        """

        healthbar_html = f"""
            <div style="{out_bar_style}">
                <div style="{in_bar_style}"></div>
            </div>
            <span>{resource}/{resource_max}</span>
        """

        return format_html(healthbar_html)

    def health(self, obj):
        return self.resource_bar(obj=obj.statistics, resource="health", color="green")

    def mana(self, obj):
        return self.resource_bar(obj=obj.statistics, resource="mana", color="blue")

    def exp(self, obj):
        return self.resource_bar(obj=obj, resource="experience", color="#4b84de")

    def gold_(self, obj):
        gold_style = f"""
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: #f5d142;
            display: inline-block;
            margin-right: 5px;
        """
        gold_html = f"""
            <div style="{gold_style}"></div><span>{obj.gold}</span> 
        """

        return format_html(gold_html)


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = "name", "icon_", "rarity", "bonus", "held_by"
    search_fields = ("name",)
    list_filter = "rarity", "boosted_stat"

    def icon_(self, obj):
        style = f"""
            width: 64px;
            height: 64px;
            border-radius: 10px;
            box-shadow: 0px 0px 5px 5px {obj.rarity.color};
        """
        icon_html = f"""
            <img src="{settings.MEDIA_URL}{obj.icon.name}" style="{style}" />
        """
        return format_html(icon_html)

    def bonus(self, obj):
        return f"+{obj.value} {obj.boosted_stat}"

    # shortcut to a related object
    def held_by(self, obj):
        a_html = f"""
            <a href="{reverse('admin:rpg_character_change', kwargs={"object_id": obj.character.pk})}">{obj.character}</a>
        """
        return format_html(a_html)
