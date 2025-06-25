from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from appshop.models import Contact, Product, NetworkLink
from appshop.serializers import ContactSerializer, ProductSerializer, NetworkLinkSerializer, NetworkLinkDetailSerializer


class IsStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NetworkLinkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffPermission]
    # queryset = NetworkLink.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['contacts__country', 'type']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NetworkLinkDetailSerializer
        return NetworkLinkSerializer

    def get_queryset(self):
        return NetworkLink.objects.select_related('contacts').prefetch_related('products')
