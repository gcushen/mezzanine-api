from rest_framework import serializers
from django.template.defaultfilters import strip_tags
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
from mezzanine.generic.models import Comment
from mezzanine.conf import settings


class PrivateField(serializers.ReadOnlyField):
    """
    A Serializer Field class that can be used to hide sensitive User data in the JSON output
    """

    def get_attribute(self, instance):
        if instance.id == self.context.get('request').user.id or self.context.get('request').user.is_superuser:
            return super(PrivateField, self).get_attribute(instance)
        return None


class SiteSerializer(serializers.ModelSerializer):
    """
    Serializing public site data
    """
    title = serializers.SerializerMethodField('get_site_title')
    tagline = serializers.SerializerMethodField('get_site_tagline')
    settings.use_editable()

    def get_site_title(self, obj):
        return settings.SITE_TITLE

    def get_site_tagline(self, obj):
        return settings.SITE_TAGLINE

    class Meta(object):
        model = Site
        fields = ['title', 'tagline', 'domain']


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


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializing all the comments
    """
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_name', 'comment', 'submit_date', 'is_public', 'is_removed']


class PageSerializer(serializers.ModelSerializer):
    """
    Serializing all the pages
    """
    content = serializers.SerializerMethodField('get_page_content')
    meta_description = serializers.CharField(source='description', read_only=True)
    tags = serializers.CharField(source='keywords_string', read_only=True)

    def get_page_content(self, obj):
        if obj.content_model == 'richtextpage':
            return obj.richtextpage.content
        elif obj.content_model == 'form':
            return obj.form.content
        else:
            return None

    class Meta:
        model = Page
        fields = ('id', 'parent', 'title', 'content', 'content_model', 'slug', 'publish_date',
                  'login_required', 'meta_description', 'tags')


class PostInputSerializer(serializers.ModelSerializer):
    """
    Serializing write access to blog posts
    """
    # `categories` input should be a comma delimited list
    categories = serializers.CharField(required=False)

    def create(self, validated_data):
        try:
            categories = validated_data.pop("categories")
        except KeyError:
            categories = None

        initial = {
            "title": validated_data.pop("title"),
            "user": self.context['request'].user,
        }
        post = Post.objects.create(**initial)

        for k, v in validated_data.items():
            setattr(post, k, v)

        if categories:
            for name in categories.split(','):
                name = name.strip()
                cat, created = BlogCategory.objects.get_or_create(title=name)
                post.categories.add(cat)

        post.save()
        return post

        # TODO: Handle updating the `categories` field of blog posts using flat representation as above
        # ...

    class Meta:
        model = Post
        # TODO: fix 'categories' incorrectly showing 'blog.BlogCategory.None' after creating blog post with categories
        fields = ('id', 'title', 'content', 'categories', 'status', 'publish_date', 'expiry_date', 'allow_comments')


class PostOutputSerializer(serializers.ModelSerializer):
    """
    Serializing read access to blog posts
    """
    user = UserSerializer(required=False, read_only=True)
    categories = CategorySerializer(many=True, required=False, read_only=True)
    url = serializers.URLField(source='get_absolute_url_with_host', read_only=True)
    tags = serializers.CharField(source='keywords_string', read_only=True)
    short_url = serializers.CharField(source='get_absolute_url', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    excerpt = serializers.SerializerMethodField()

    def get_excerpt(self, obj):
        return strip_tags(obj.description_from_content())

    class Meta:
        model = Post
        fields = ('id', 'user', 'publish_date', 'updated', 'title',  'content', 'excerpt', 'slug', 'url', 'short_url',
                  'categories', 'allow_comments', 'comments_count', 'comments', 'tags', 'featured_image')
