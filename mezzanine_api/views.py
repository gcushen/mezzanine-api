from rest_framework import viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, PostSerializer, CategorySerializer, PageSerializer
from django.contrib.auth.models import User
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
import django_filters
# from django.contrib.sites.models import Site
# from mezzanine.generic.models import ThreadedComment
# from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


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
    permission_classes = (permissions.IsAdminUser,)


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
    ---
    list:
        parameters:
            - name: search
              type: string
              description: Search for category names that match the query
              paramType: query
    """
    queryset = BlogCategory.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    serializer_class = CategorySerializer
    pagination_class = CustomPagination


class PostFilter(django_filters.FilterSet):
    """
    A class for filtering blog posts.
    """
    category = django_filters.NumberFilter(name="categories")
    user = django_filters.NumberFilter(name="user__id")
    username = django_filters.CharFilter(name="user__username")

    class Meta:
        model = Post
        fields = ['category', 'username', 'user']


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    For listing or retrieving blog posts.
    ---
    list:
        parameters:
            - name: category
              type: integer
              description: Filter posts by category ID
              paramType: query
            - name: user
              type: integer
              description: Filter posts by user ID
              paramType: query
            - name: username
              type: string
              description: Filter posts by username
              paramType: query
            - name: search
              type: string
              description: Search for blog posts that match the query
              paramType: query
    """
    queryset = Post.objects.all().order_by("-publish_date")
    filter_class = PostFilter
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title', 'content',)
    serializer_class = PostSerializer
    pagination_class = CustomPagination
