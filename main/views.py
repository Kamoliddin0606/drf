from rest_framework import mixins
from requests import request
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category
from django.forms import model_to_dict
from rest_framework.viewsets import GenericViewSet
from .serializers import PostSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.permissions import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
# _______10-dars permissions  uchun ishlatildi start__________
class PostGetAPIView(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    
    permission_classes=[IsAuthenticatedOrReadOnly]

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[IsOwnerOrReadOnly]

class PostRemoveAPIView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[IsAdminOrReadOnly]
# _______10-dars permissions  uchun ishlatildi end__________

# class PostAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CategoryAPIList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset=Post.objects.all()
#     serializer_class = PostSerializer
# class PostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Post.objects.all()
#     serializer_class = PostSerializer

# # _______9-darsgacha bo`lgan mavzular uchun ishlatildi end__________
# class PostAPIViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     def get_queryset(self):
#         pk = self.kwargs.get('pk',None)
#         if  pk:
#             return Post.objects.filter(pk=pk)
           
#         return Post.objects.all()[:3]
#     @action(methods=['get'], detail=True)
#     def categorydetail(self, request, pk=None):
#         if not pk:
            
#             return Response({'error':'category pk not found'})
#         else:

#             category = Category.objects.get(pk=pk)
#             return Response({'categories':category.title})
#     @action(methods=['get'], detail=False)
#     def category(self, request):
      
#         categories = Category.objects.all()
#         return Response({'categories':[category.title for category in categories]})
 
        
# # _______9-darsgacha bo`lgan mavzular uchun ishlatildi end__________

# class PostAPIView(APIView):
   
#     def get(self,request):
#         dictObjects = Post.objects.all()
#         return  Response({'test':PostSerializer(dictObjects,many=True).data})

#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         # postNew = Post.objects.create(
#         #     title=request.data['title'],
#         #     author=request.data['author'],
#         #     category_id=request.data['category_id']
#         # )

#         # return Response({'post':PostSerializer(postNew).data})
#         return Response({'post':serializer.data})
   
#     def put(self, request, *args, **kwargs):
#         print(kwargs, request.data)
#         pk = kwargs.get('pk',None)
   
#         if not pk:
#             return Response({'error':'Method PUT is not allowed'})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({'post':"Object is not found"})

#         serializer = PostSerializer(instance=instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post':serializer.data})
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         print(request.data)
#         if not pk:
#             return Response({'error':"Method DELETE is not allowed"})
#         Post.objects.get(pk=pk).delete()    
#         return Response({'delete':pk})


