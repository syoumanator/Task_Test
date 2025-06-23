from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=15,
        verbose_name="Username",
        help_text="Введите имя пользователя",
    )
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите адрес электронной почты"
    )
    city = models.CharField(
        max_length=30,
        verbose_name="City",
        help_text="Укажите город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Avatar", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
