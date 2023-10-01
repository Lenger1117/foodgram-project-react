from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = "Управление пользователями"


class AdminConfig(AppConfig):
    def ready(self):
        from django.contrib import admin
        from rest_framework.authtoken.models import Token
        admin.site.unregister(Token)
