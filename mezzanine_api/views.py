from rest_framework import generics, permissions
from .serializers import UserSerializer, PostSerializer, CategorySerializer, PageSerializer
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
from mezzanine.generic.models import ThreadedComment


class UserList(generics.ListAPIView):
    """
    API endpoint that allows all users to be viewed
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows a specific user to be viewed
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class CategoryList(generics.ListAPIView):
    """
    API endpoint that allows all categories to be viewed
    """
    
    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows a specific category to be viewed
    """
    
    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class PageList(generics.ListAPIView):
    """
    API endpoint that allows all pages to be viewed
    """
    
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows a specific page to be viewed
    """
    
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'id'

class PostList(generics.ListAPIView):
    """
    API endpoint that allows all blog posts to be viewed
    """
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    """
    API endpoint that allows a specific blog post to be viewed
    """
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
