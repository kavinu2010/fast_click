from django.urls import path 
from .views import TdList,CreatList,DetailList,UpdateList

urlpatterns=[
  path('',TdList.as_view(),name='tdlist'),
  path('list/<int:pk>/', DetailList.as_view(), name='list'),  
  path('create/',CreatList.as_view(),name='create'),
  path('list-update/<int:pk>/',UpdateList.as_view(),name='list-update'),
]