from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'favorite')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'

    @admin.display(empty_value='unknown')
    def favorites(self, obj):
         return obj.favorite


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
