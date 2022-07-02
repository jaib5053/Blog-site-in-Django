from django.utils.text import slugify

from .models import *
import string
import random

def generate_random_string(n):
    res = ''.join(random.choices(string.ascii_uppercase+string.digits, k=n))
    return res

def generate_slug(text):
    new_slug=slugify(text)
    if BlogPost.object.filter(slug=new_slug).exists():
        generate_slug(text+ generate_random_string(5))
    return new_slug

def return_categories():
    mycats = Category.objects.all()
    return mycats