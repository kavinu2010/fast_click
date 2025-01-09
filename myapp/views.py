from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from .models import TodoList
from django.urls import reverse_lazy



class TdList(ListView):
  model=TodoList
  context_object_name='tdlist'


class DetailList(DetailView):
    model = TodoList
    context_object_name = 'list'

 
 
class CreatList(CreateView):
  model=TodoList
  fields='__all__'
  success_url=reverse_lazy('tdlist')

class UpdateList(UpdateView):
   model=TodoList
   fields='__all__'
   success_url=reverse_lazy('tdlist')

   
