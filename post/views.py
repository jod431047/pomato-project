from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
class BrandList(generic.ListView):
    model  = Post
    
    
    
    
def about(request):
    return render(request,'post/about.html',{})

def home(request):
    brands = Post.objects.all()
    return render(request, 'post/home.html',{'brands':brands})     