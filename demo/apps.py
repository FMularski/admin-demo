from django.contrib.admin.apps import AdminConfig


class RPGAdminConfig(AdminConfig):
    default_site = "demo.admin.RPGAdminSite"
