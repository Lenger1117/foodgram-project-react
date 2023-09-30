from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser
from django.contrib.admin.utils import quote
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse

from rest_framework.authtoken.models import Token, TokenProxy

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'


class TokenChangeList(ChangeList):
    def url_for_result(self, result):
        pk = result.user.pk
        return reverse('admin:%s_%s_change' % (self.opts.app_label,
                                               self.opts.model_name),
                       args=(quote(pk),),
                       current_app=self.model_admin.admin_site.name)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    fields = ('user',)
    ordering = ('-created',)
    actions = None

    def get_changelist(self, request, **kwargs):
        return TokenChangeList

    def get_object(self, request, object_id, from_field=None):
        queryset = self.get_queryset(request)
        field = User._meta.pk
        try:
            object_id = field.to_python(object_id)
            user = User.objects.get(**{field.name: object_id})
            return queryset.get(user=user)
        except (queryset.model.DoesNotExist, User.DoesNotExist,
                ValidationError, ValueError):
            return None

    def delete_model(self, request, obj):
        token = Token.objects.get(key=obj.key)
        return super().delete_model(request, token)


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
