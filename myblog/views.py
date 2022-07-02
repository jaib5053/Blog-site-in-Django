from ast import Num
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogPost

def index(request):
   myposts=BlogPost.objects.all()
   return render(request,'index.html',{'myposts':myposts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("This is contact us page")

def post(request, id):
    post = BlogPost.objects.filter(post_id=id) [0]
    return render(request,'post.html',{'post': post})