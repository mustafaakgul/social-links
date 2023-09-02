from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.accounts.models import Profile
from apps.links.models import Link


class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = (
            'id',
            'title',
            'url',
        )


class ProfileSerializer(ModelSerializer):
    links = LinkSerializer(many=True)
    depth = 3

    class Meta:
        model = Profile
        fields = (
            'id',
            'bio',
            'birth_date',
            'location',
            'links',
        )


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    depth = 3

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'profile',
        )

    # def validate_email(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #         raise serializers.ValidationError({"email": "This email is already in use."})
    #     return value
    #
    # def validate_username(self, value):
    #     user = self.context['request'].user
    #     if User.objects.exclude(pk=user.pk).filter(username=value).exists():
    #         raise serializers.ValidationError({"username": "This username is already in use."})
    #     return value

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        profile_serializer = ProfileSerializer(instance.profile, data=profile)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, attr):
        validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        user = User.objects.create(
                username = validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user
