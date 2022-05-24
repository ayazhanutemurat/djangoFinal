import json
import re

from rest_framework import serializers

from authorization.models import User
from books.constants import USER_ROLES


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'avatar']

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)


class UserDetailsSerializer(UserSerializer):
    roles = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ['roles', 'username', 'email', 'is_active', 'date_joined']

    def get_roles(self, obj):
        roles = dict(USER_ROLES)
        return roles[obj.roles]


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def save(self):
        User.objects.create_user(self.validated_data['username'],
                                 self.validated_data['password'],
                                 self.validated_data['email'],
                                 self.validated_data['first_name'],
                                 self.validated_data['last_name'])





