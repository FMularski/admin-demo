
from rest_framework import authentication, generics

from commander import models, serializers


class AdminCommanderAPIView(generics.CreateAPIView):
    """
    Executes the command and creates a log.
    """

    authentication_classes = [authentication.SessionAuthentication]
    queryset = models.AdminCommanderLog.objects.all()
    serializer_class = serializers.AdminCommanderLogSerializer