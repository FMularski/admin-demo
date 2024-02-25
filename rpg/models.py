from colorfield.fields import ColorField
from django.db import models


class Guild(models.Model):
    name = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Statistics(models.Model):
    base_health = models.IntegerField(default=100)
    base_max_health = models.IntegerField(default=100)
    base_mana = models.IntegerField(default=100)
    base_max_mana = models.IntegerField(default=100)
    base_strength = models.IntegerField(default=10)
    base_intelligence = models.IntegerField(default=10)
    base_agility = models.IntegerField(default=10)


class Quest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=100)
    character_class = models.ForeignKey(
        CharacterClass, on_delete=models.PROTECT, related_name="characters"
    )
    statistics = models.OneToOneField(
        Statistics, on_delete=models.PROTECT, related_name="character"
    )
    guild = models.ForeignKey(Guild, on_delete=models.PROTECT, related_name="characters")
    gold = models.PositiveIntegerField(default=0)
    quests = models.ManyToManyField(Quest, related_name="characters")
    level = models.PositiveSmallIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    experience_level_up = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.character_class} {self.name} [Lv. {self.level}]"


class Rarity(models.Model):
    COLOR_PALETTE = [
        (
            "#287d38",
            "green",
        ),
        (
            "#305bd1",
            "blue",
        ),
        (
            "#631e9c",
            "purple",
        ),
        (
            "#ed9f32",
            "orange",
        ),
    ]

    name = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField()
    color = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return self.name


class StatisticsChoices(models.TextChoices):
    health = ("health", "Health")
    mana = ("mana", "Mana")
    strength = ("strength", "Strength")
    intelligence = ("intelligence", "Intelligence")
    agility = ("agility", "Agility")


class Item(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.ForeignKey(Rarity, on_delete=models.PROTECT, related_name="items")
    boosted_stat = models.CharField(max_length=20, choices=StatisticsChoices.choices)
    value = models.IntegerField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name
