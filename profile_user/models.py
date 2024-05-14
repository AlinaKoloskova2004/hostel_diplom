
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    bio = models.TextField(blank=True, verbose_name='Описание')
    location = models.CharField(max_length=100, blank=True, verbose_name='Город')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, verbose_name='Фото профиля')

    def __str__(self):
        return self.user.username