from rest_framework import serializers

from auth_app.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'given_name', 'last_name', 'email', 'role']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        name_value = representation.pop("given_name") + " " + representation.pop("last_name")
        representation.update(name=name_value)

        type_value = representation.pop("role")
        representation.update(type=type_value)

        return representation

