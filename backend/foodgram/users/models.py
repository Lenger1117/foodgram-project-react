from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='Почта',
        unique=True
        )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
        blank=False
        )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
        blank=False
        )
    username = models.CharField(max_length=150, verbose_name='Логин')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Подписчик',
                             related_name='follower')
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='author')

    class Meta:
        constraints = [UniqueConstraint
                       (fields=['user', 'author'],
                        name='user_author_unique')]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self) -> str:
        return f'{self.user} подписался на пользователя {self.author}'
