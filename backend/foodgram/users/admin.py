from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser
from rest_framework.authtoken.models import Token


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):

    def get_model_perms(self, request):
        return {}


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
