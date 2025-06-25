from django.db import models


class Contact(models.Model):
    """Модель контакта"""

    email = models.EmailField(max_length=20, verbose_name="Email")
    country = models.CharField(max_length=20, verbose_name="Country")
    city = models.CharField(max_length=50, verbose_name="City")
    street = models.CharField(max_length=150, verbose_name="Street")
    house_number = models.PositiveSmallIntegerField(verbose_name="House number")

    def __str__(self):
        return f"{self.email} из {self.country}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["email", "country"]


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=50, verbose_name="Name")
    model = models.CharField(max_length=50, verbose_name="Model")
    date_release = models.DateField(verbose_name="Date release")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
