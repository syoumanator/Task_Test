from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        )
