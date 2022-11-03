from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Class of model for user account"""
    # user base model User, delete CASCADE, revert attr for model "profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                      related_name="profile", 
                                      verbose_name='Имя пользователя')
    # field for desc,
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    # exmpl city
    location = models.CharField(max_length=30, blank=True, verbose_name='Местоположение')
    # date of registy
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    # if object updated it takes date of this event
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    # flag, by default all user have flag simple user.
    simple_user = models.BooleanField(default=True, verbose_name='Простой пользователь?')
    # file for user photo
    photo = models.ImageField(upload_to=r'photos/%Y/%m/%d')

    def __str__(self):
        return self.user.username
    

    class Meta:
        # setting admin panel
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        ordering = ['date_joined', 'user']

