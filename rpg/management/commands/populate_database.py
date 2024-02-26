from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Populate the demo database."

    fixtures = [
        "guild.json",
        "quest.json",
        "characterclass.json",
        "statistics.json",
        "character.json",
        "rarity.json",
        "item.json",
    ]

    def _create_admin(self):
        User.objects.create_superuser(username="admin", password="admin")

    def handle(self, *args, **options):
        self._create_admin()

        for fixture in self.fixtures:
            call_command("loaddata", fixture)

        self.stdout.write(self.style.SUCCESS("Database populated."))
