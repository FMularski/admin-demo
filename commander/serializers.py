import io

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import CommandError
from rest_framework import serializers

from . import models

User = get_user_model()


class AdminCommanderLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdminCommanderLog
        fields = ("command",)

    def create(self, validated_data):
        log = models.AdminCommanderLog.objects.create(
            user=self.context["request"].user, command=validated_data["command"]
        )

        command, *args = validated_data["command"].split(" ")

        try:
            with io.StringIO() as out:
                call_command(command, *args, stdout=out)
                log.output = out.getvalue()
        except CommandError as e:
            log.output = str(e)

        log.save()

        return log

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["output"] = instance.output

        return representation
