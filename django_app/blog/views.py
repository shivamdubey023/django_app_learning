from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Blog Home Page")

def about(request):
    return HttpResponse("Blog About Page")

def get_post_detail(request, post_id):
    return HttpResponse(f"This is the detail page for post with id {post_id}")  

def get_post_by_category(request, category_name):
    return HttpResponse(f"This is the page for posts in category {category_name}")  

# def article_detail(request, year, month, day, slug):
#     return HttpResponse(f"This is the detail page for article with slug '{slug}' published on {year}-{month}-{day}")
def article_detail(request,**kwargs):
    return HttpResponse(f"This is the detail page for article published on {kwargs}")

def article_year(request, year):
    return HttpResponse(f"This is the page for articles published in the year {year}")

def sum(request):
    a = 5
    b = 10
    return HttpResponse(f"The sum of a ={a} and b = {b} is {a+b}")