from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from matplotlib import image
from sqlalchemy import true

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class BlogPost(models.Model):
    post_id=models.AutoField(primary_key=true)
    post_title=models.CharField(max_length=200)
    post_slug=models.CharField(max_length=200)
    post_content=models.TextField(max_length=2000)
    post_date=models.DateField(auto_now_add=true)
    post_image=models.ImageField(upload_to='static/blog_img')
    post_category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    featured=models.BooleanField(default=0)

    def __str__(self):
        return self.post_title

