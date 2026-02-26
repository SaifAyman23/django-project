from django.apps import AppConfig


class dashboardAdminConfig(AppConfig):
    name = "dashboard"
    default = True

    def ready(self):
        import dashboard.signals  # NOQA
