from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, PostSerializer, CategorySerializer, PageSerializer
from django.contrib.auth.models import User
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
#from django.contrib.sites.models import Site
#from mezzanine.generic.models import ThreadedComment


class CustomPagination(PageNumberPagination):
    """
    Let large result sets be split into individual pages of data
    """
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    For listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination


class PageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    For listing or retrieving pages.
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = CustomPagination


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    For listing or retrieving blog categories.
    """
    queryset = BlogCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    For listing or retrieving blog posts.
    """
    queryset = Post.objects.all().order_by("-publish_date")
    filter_fields = ('categories',)
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = PostSerializer
    pagination_class = CustomPagination
