from ast import Num
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogPost, Contact
from django.core.paginator import Paginator


def index(request):
   posts=BlogPost.objects.all()
   paginator = Paginator(posts, 5)
   page_number = request.GET.get('page')
   myposts = paginator.get_page(page_number)

   return render(request,'index.html',{'myposts':myposts})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','' )
        email=request.POST.get('email','' )
        subject=request.POST.get('subject','' )
        message=request.POST.get('message','' )
        details=Contact(contact_name=name, contact_email=email, contact_subject=subject, contact_msg=message)
        details.save()
    return render(request,'contact.html')

def post(request, slug):
    post = BlogPost.objects.filter(post_slug=slug) [0]
    return render(request,'post.html',{'post': post})