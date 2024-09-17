from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import * 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# For Api
from rest_framework import viewsets
from .serializers import BlogSerializer, BlogCategorySerializer

# Create your views here.
def home(request):
    blog_list = Blog.objects.all().order_by('-created')
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get("page")
    try:
        blogs = paginator.get_page(page_number)
    except PageNotAnInteger:
        blogs = paginator.get_page(1)
    except EmptyPage:
        blogs = paginator.get_page(paginator.num_pages)
    
    context = {'blogs':blogs}
    
    return render(request, 'Blog/home.html', context=context)

def category_page(request, category_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    blog_list = Blog.objects.filter(category = category).order_by('-created')
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get("page")
    try:
        blogs = paginator.get_page(page_number)
    except PageNotAnInteger:
        blogs = paginator.get_page(1)
    except EmptyPage:
        blogs = paginator.get_page(paginator.num_pages)
    
    context = {'category':category, 'blogs':blogs}

    return render(request, 'Blog/category.html', context = context)


def blog_details(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    context = {'blog':blog}

    return render(request, 'Blog/blog_details.html', context=context)


# api views
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    