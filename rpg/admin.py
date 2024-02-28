from django.contrib import admin

from rpg import models


@admin.register(models.Guild)
class GuildAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Quest)
class QuestAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rarity)
class RarityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
