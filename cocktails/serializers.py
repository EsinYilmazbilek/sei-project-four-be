from rest_framework import serializers
from django.contrib.auth import get_user_model



from .models import Cocktail, Comment, Save
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

class SaveSerializer(serializers.ModelSerializer):
  '''Serializer for saving cocktails'''
  class Meta:
    model = Save
    fields = '__all__'

class NestedSaveSerializer(serializers.ModelSerializer):
  '''Nested Save Serializer'''
  owner = NestedUserSerializer()

  class Meta:
    model = Save
    fields = '__all__'

# class CommentLikeSerializer(serializers.ModelSerializer):
#   '''comments like serializer'''
#   class Meta:
#     model = CommentLike
#     fields = '__all__'

# class NestedCommentLikeSerializer(serializers.ModelSerializer):
#   '''Nested comment like serializer'''
#   owner = NestedCommentSerializer()

#   class Meta:
#     model = CommentLike
#     fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    ''' Serializer for Comments'''
    # liked_by = NestedCommentLikeSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class CocktailSerializer(serializers.ModelSerializer):
    ''' Serializer for Cocktail '''
    comments = NestedCommentSerializer(many=True, read_only=True)
    saved_by = NestedSaveSerializer(many=True, read_only=True)
    
  

    class Meta:
        model = Cocktail
        fields = '__all__'

