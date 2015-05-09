from rest_framework import serializers
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
from mezzanine.generic.models import ThreadedComment


class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the users
    """
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializing all the categories
    """
    
    class Meta:
        model = BlogCategory
        fields = ('id', 'title', 'slug')


class PageSerializer(serializers.ModelSerializer):
    """
    Serializing all the pages
    """
    
    class Meta:
        model = Page
        fields = ('id', 'parent', 'title', 'description', 'slug')


class PostSerializer(serializers.ModelSerializer):
    """
    Serializing all the blog posts
    """
    
    user = UserSerializer(required=False)
    categories = CategorySerializer(many=True, required=False, read_only=True)
    url = serializers.URLField(source='get_absolute_url_with_host', read_only=True)
    short_url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'publish_date', 'updated', 'title', 'url', 'short_url', 'content', 'slug',
                  'categories', 'allow_comments', 'comments_count', 'keywords_string', 'featured_image')

