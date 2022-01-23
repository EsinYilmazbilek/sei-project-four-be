from django.shortcuts import render

# Create your views here.

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Cocktail, Comment
from .serializers import CocktailSerializer, CommentSerializer
from .permissions import isOwnerOrReadOnly

class CocktailListView(ListCreateAPIView):
    ''' View for /cocktail endpoint GET/POST '''
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CocktailDetailView(RetrieveUpdateDestroyAPIView):
    ''' View for /cocktail/id endpoint GET/PUT/PATCH/DELETE '''
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentListView(CreateAPIView):
    ''' View for /cocktail/id/comments POST '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class CommentDetailView(DestroyAPIView):
    ''' View for /cocktail/id/comments/id DELETE '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (isOwnerOrReadOnly, )