from rest_framework import serializers

from appshop.models import Contact, Product, NetworkLink


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class NetworkLinkSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactSerializer(read_only=True)

    class Meta:
        model = NetworkLink
        read_only_fields = ['credit']
        exclude = ['created_at']


class NetworkLinkDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactSerializer(read_only=True)

    class Meta:
        model = NetworkLink
        fields = '__all__'
        read_only_fields = ['credit']
