from rest_framework import serializers
from django.contrib.auth import get_user_model



from .models import Cocktail, Comment
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class NestedCommentSerializer(serializers.ModelSerializer):
    ''' Serializer for nested comments'''
    owner = NestedUserSerializer()

    class Meta:
      model = Comment
      fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    ''' Serializer for Comments'''
    class Meta:
        model = Comment
        fields = '__all__'

class CocktailSerializer(serializers.ModelSerializer):
    ''' Serializer for Cocktail '''
    comments = NestedCommentSerializer(many=True, read_only=True)
    class Meta:
        model = Cocktail
        fields = '__all__'

