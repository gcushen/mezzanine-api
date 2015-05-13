from rest_framework import serializers
from django.contrib.auth.models import User
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
# from django.contrib.sites.models import Site
# from mezzanine.generic.models import ThreadedComment


class PrivateField(serializers.ReadOnlyField):
    """
    A custom Serializer Field class that can be used to hide sensitive User data in the JSON output
    """

    def get_attribute(self, instance):
        if instance.id == self.context.get('request').user.id or self.context.get('request').user.is_superuser:
            return super(PrivateField, self).get_attribute(instance)
        return None


class UserSerializer(serializers.ModelSerializer):
    """
    Serializing all the users
    """
    email = PrivateField()

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
        description_from_content = serializers.CharField(source='description_from_content', read_only=True)
        fields = ('id', 'parent', 'title', 'description', 'description_from_content', 'slug')


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
