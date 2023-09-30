from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'


class TokenAdminn(TokenAdmin):
    list_display = ('user', 'created')


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Token, TokenAdminn)
admin.site.unregister(Group)
