from django.contrib import admin
from appshop.models import Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )
    list_filter = (
        "country",
        "city",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "model",
                    "date_release"
                    )
    list_filter = (
        "name",
        "date_release"
    )
    search_fields = (
        "name",
    )
