from django.contrib import admin
from appshop.models import Contact


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
