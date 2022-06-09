from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category')

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
