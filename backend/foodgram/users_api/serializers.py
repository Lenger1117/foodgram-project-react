from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.fields import SerializerMethodField
from users.models import CustomUser, Follow


class CreateCustomUserSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class CustomUserSerializer(UserSerializer):
    is_subscribed = SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'is_subscribed']

    def get_is_subscribed(self, object):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Follow.objects.filter(user=user, author=object.id).exists()
