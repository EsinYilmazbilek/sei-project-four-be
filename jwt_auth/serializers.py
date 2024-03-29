from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.conf import settings

from cocktails.models import Cocktail, Comment, CommentLike, Save

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confiratmion do not match'})

        if settings.ENV != 'DEV':
            try:
                validation.validate_password(password=password)
            except ValidationError as err:
                raise ValidationError({'password': err})

        attrs['password'] = make_password(password)

        return attrs

    class Meta:
        model = User
        fields = '__all__'


class NestedCocktailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'image')


class NestedCommentSerializer(serializers.ModelSerializer):
    cocktail = NestedCocktailSerializer()

    class Meta:
        model = Comment
        fields = '__all__'

class NestedSaveSerializer(serializers.ModelSerializer):
    cocktail = NestedCocktailSerializer()

    class Meta:
        model = Save
        fields = '__all__'
class NestedCommentLikeSerializer(serializers.ModelSerializer):
    comment = NestedCommentSerializer()
    
    class Meta:
      model = CommentLike
      fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    comments_posted = NestedCommentSerializer(many=True)
    saved_cocktail = NestedSaveSerializer(many=True)
    liked_comment = NestedCommentLikeSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image', 'comments_posted', 'saved_cocktail', 'liked_comment')