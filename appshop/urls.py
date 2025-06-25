from rest_framework.routers import DefaultRouter
from appshop.apps import AppshopConfig
from appshop.views import ContactViewSet, ProductViewSet

app_name = AppshopConfig.name

contact_router = DefaultRouter()
contact_router.register(r"contacts", ContactViewSet, basename="contacts")

product_router = DefaultRouter()
product_router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [] + contact_router.urls + product_router.urls
