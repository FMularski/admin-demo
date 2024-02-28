from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AdminCommanderLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_commander_logs")
    created_at = models.DateTimeField(auto_now_add=True)
    command = models.CharField(max_length=1024)
    output = models.TextField(null=True, blank=True)

    @property
    def full_command(self):
        return "python3 manage.py " + self.command

    def __str__(self):
        return f"{self.user} {self.created_at} {self.full_command}"
