from django.urls import path
from .views import (
    CocktailListView,
    CocktailDetailView,
    CommentListView,
    CommentDetailView,
)

urlpatterns = [
    path('', CocktailListView.as_view()),
    path('<int:pk>/', CocktailDetailView.as_view()),
    path('<int:pk>/comments/', CommentListView.as_view()),
    path('<int:cocktail_pk>/comments/<int:pk>/', CommentDetailView.as_view()),
]