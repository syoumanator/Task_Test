from django.contrib import admin
from appshop.models import Contact, Product, NetworkLink
from django.urls import reverse
from django.utils.html import format_html


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
    list_display = ("name", "model", "date_release")
    list_filter = ("name", "date_release")
    search_fields = ("name",)


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contacts",
        "type",
        "products_list",
        "provider",
        "credit",
        "created_at",
    )
    list_filter = ("name", "contacts__city",)
    actions = ("credit_clear",)
    readonly_fields = ("provider_link",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('contacts')

    def credit_clear(self, request, queryset):
        obj = queryset.update(credit=0)
        self.message_user(request, f"Задолженность очищена у {obj}.")

    credit_clear.short_description = "Обнулить задолженность"

    def provider_link(self, obj):
        if obj.provider:
            url = reverse("admin:appshop_networklink_change", args=[obj.provider.id])
            return format_html('<a href="{}">{}</a>', url, obj.provider.name)
        return '_'
    provider_link.short_description = "Ссылка поcтавщика"

    def products_list(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    products_list.short_description = "Список продуктов"
