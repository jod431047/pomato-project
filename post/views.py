from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
class PostList(generic.ListView):
    model  = Post