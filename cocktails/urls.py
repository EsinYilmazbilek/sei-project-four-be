from django.urls import path
from .views import (
    CocktailListView,
    CocktailDetailView,
    CommentListView,
    CommentDetailView,
    SaveListView,
    SaveDetailView,
    CommentLikeListView,
    CommentLikeDetailView,
)

urlpatterns = [
    path('', CocktailListView.as_view()),
    path('<int:pk>/', CocktailDetailView.as_view()),
    path('<int:pk>/comments/', CommentListView.as_view()),
    path('<int:cocktail_pk>/comments/<int:pk>/', CommentDetailView.as_view()),
    path('<int:pk>/saved/', SaveListView.as_view()),
    path('<int:cocktail_pk>/saved/<int:pk>/', SaveDetailView.as_view()),
    path('<int:pk>/comments/<int:comments_pk>/liked/', CommentLikeListView.as_view()),
    path('<int:cocktail_pk>/comments/<int:comments_pk>/liked/<int:pk>/', CommentLikeDetailView.as_view())
]