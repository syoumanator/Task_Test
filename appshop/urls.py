# from django.urls import path
from rest_framework.routers import DefaultRouter
from appshop.apps import AppshopConfig
from appshop.views import ContactViewSet

app_name = AppshopConfig.name

contact_router = DefaultRouter()
contact_router.register(r"contacts", ContactViewSet, basename="contacts")

urlpatterns = [] + contact_router.urls
