from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=10)
    is_admin = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        instance.name = validated_data.get('name',instance.name)
        instance.is_admin = validated_data.get('is_admin',instance.is_admin)
        instance.is_superuser = validated_data.get('is_superuser',instance.is_superuser)
        instance.save()
        return instance
