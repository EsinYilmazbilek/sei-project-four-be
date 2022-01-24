from django.db import models

# Create your models here.

class Cocktail(models.Model):
    ''' Cocktail Model '''
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    about = models.TextField(max_length=300)
    serves = models.PositiveIntegerField()
    ingredients = models.CharField(max_length=350)
    recipe = models.TextField(max_length=1000)
    

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    ''' Comment Model '''
    content = models.TextField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    cocktail = models.ForeignKey(
        Cocktail,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
    'jwt_auth.User',
    related_name='comments_posted',
    on_delete=models.CASCADE
  )

    def __str__(self):
        return f'Comment {self.id} on {self.cocktail}'

class Save(models.Model):
  '''Save Model'''
  created_at = models.DateTimeField(auto_now_add=True)
  cocktail = models.ForeignKey(
    Cocktail,
    related_name='saved_by',
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    'jwt_auth.User',
    related_name='saved_cocktail',
    on_delete=models.CASCADE
  )
  def __str__(self):
    return f'Save {self.id} on cocktail {self.cocktail}'

class CommentLike(models.Model):
  '''Comments like model'''
  created_at = models.DateTimeField(auto_now_add=True)
  comment = models.ForeignKey(
    Comment,
    related_name='liked_by',
    on_delete=models.CASCADE 
  )
  owner = models.ForeignKey(
    'jwt_auth.User',
    related_name='liked_comment',
    on_delete=models.CASCADE
  )
  def __str__(self):
    return f'Like {self.id} on cocktail {self.comment}'