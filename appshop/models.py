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


class NetworkLink(models.Model):
    """Модель звена сети"""

    TYPE_CHOICES = [("factory", 'Завод'), ("retail", 'Розничная сеть'), ("entrepreneur", 'Индивидуальный предприниматель')]

    name = models.CharField(max_length=100, verbose_name="name")
    contacts = models.ForeignKey(Contact, on_delete=models.SET_NULL, related_name="contacts", verbose_name="contacts", blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, verbose_name="Type")
    products = models.ManyToManyField(Product, related_name="products", verbose_name="products")
    provider = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="provider", blank=True, null=True)
    credit = models.DecimalField( max_digits=10, decimal_places=2, verbose_name="credit", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    def __str__(self):
        return f"{self.name} - {self.type} - {self.provider}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
        ordering = ["name", "type"]
