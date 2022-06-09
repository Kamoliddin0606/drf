from ctypes.wintypes import POINT
from dataclasses import fields
from email.policy import default
import io
import json
from re import I
from turtle import title
from unicodedata import category
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.forms import model_to_dict
from rest_framework import serializers
from .models import Post, Category
# # 3-dars
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# 3-dars end
# 

# 4-dars start
class ModelPost:
    def __init__(self,title, author,category) -> None:
        self.title = title
        self.author = author
        self.category = category
class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Post
#        fields = ('title', 'author', 'category', 'active', 'body')
        fields = '__all__'

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     author = serializers.CharField(max_length=100)
#     category_id = serializers.IntegerField(min_value=1)
#     active = serializers.BooleanField()
#     body = serializers.CharField()
#     def create(self,validated_data):
#         return Post.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.body = validated_data.get('body', instance.body)
#         instance.active = validated_data.get('active',instance.active)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
        
#         instance.save()
#         return instance


def encode():
    model = ModelPost('New post with decode', 'user3', 1)
    model_sr = PostSerializer(model)

    jsonresults = JSONRenderer().render(model_sr.data)

def decode():
    stream = io.BytesIO(b'{"title":"New post with decode","author":"user3","category":1}')
    data = JSONParser().parse(stream)
    serializer = PostSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
# 4-dars end        