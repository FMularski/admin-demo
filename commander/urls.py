from django.urls import path
from . import views

urlpatterns = [
    path(
        "admin-commander/",
        views.AdminCommanderAPIView.as_view(),
        name="admin-commander",
    ),
]