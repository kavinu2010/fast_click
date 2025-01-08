from django.urls import path 
from .views import TdList,CreatList

urlpatterns=[
  path('',TdList.as_view(),name='tdlist'),
  path('create/',CreatList.as_view(),name='create'),
]