from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
