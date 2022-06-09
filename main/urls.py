from posixpath import basename
from django.urls import path, include
# from .views import CategoryAPIList, PostAPIList, PostAPIUpdate, PostAPIDetail
# from .views import PostAPIViewSet
from .views import *
from rest_framework import routers
from .routers import CustomReadOnlyRouter
# router = CustomReadOnlyRouter()
# router.register('post', PostAPIViewSet, basename='news')
# print(router.urls)
urlpatterns = [
    # -------8-darsgacha start-----
    # path('v1/postlist/',PostAPIList.as_view() ),
    # path('v1/postlist/<int:pk>/',PostAPIUpdate.as_view()),
    # path('v1/postlistdetail/<int:pk>/',PostAPIDetail.as_view()),
    # path('v1/categorylist/',CategoryAPIList.as_view())
    # -------8-darsgacha end-----

    # # ------8-dars routersiz marshrutizatsiya start-----
    # path('v1/postlist/', PostAPIViewSet.as_view({'get':'list'})),
    # path('v1/postlist/<int:pk>', PostAPIViewSet.as_view({'put':'update'})),
    # path('v1/postlistdetail/<int:pk>', PostAPIViewSet.as_view({'get':'retrieve'}))
    # # ------8-dars routersiz marshrutizatsiya end-----

    #  # -------9-darsgacha start-----
    # path('v1/', include((router.urls))) #http://127.0.0.1:8000/api/v1/post/
    #   # -------9-darsgacha end-----
    path('v1/postlist/', PostGetAPIView.as_view()),
    path('v1/postlist/<int:pk>/', PostUpdateAPIView.as_view()),
    path('v1/postlistremove/<int:pk>/', PostRemoveAPIView.as_view()),

]