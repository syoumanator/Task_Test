from rest_framework.routers import DefaultRouter

from appshop.apps import AppshopConfig
from appshop.views import ContactViewSet, NetworkLinkViewSet, ProductViewSet

app_name = AppshopConfig.name

contact_router = DefaultRouter()
contact_router.register(r"contacts", ContactViewSet, basename="contacts")

product_router = DefaultRouter()
product_router.register(r"products", ProductViewSet, basename="products")

network_link_router = DefaultRouter()
network_link_router.register(
    r"chain_links", NetworkLinkViewSet, basename="network_link"
)

urlpatterns = [] + contact_router.urls + product_router.urls + network_link_router.urls
