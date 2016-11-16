from django.core.urlresolvers import NoReverseMatch
from django.template.defaultfilters import strip_tags
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from mezzanine.blog.models import BlogPost as Post, BlogCategory
from mezzanine.pages.models import Page
from mezzanine.generic.models import Comment
from mezzanine.conf import settings
from mezzanine.utils.sites import current_request

from rest_framework import serializers


class PrivateField(serializers.ReadOnlyField):
    """
    A Serializer Field class that can be used to hide sensitive User data in the JSON output
    """

    # user needs to be got a diff way for client credentials auth
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
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')


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
    gallery_items = serializers.SerializerMethodField('get_gallery_content')

    def get_page_content(self, obj):
        if obj.content_model == 'richtextpage':
            return obj.richtextpage.content
        elif obj.content_model == 'form':
            return obj.form.content
        else:
            return None

    def get_gallery_content(self, obj):
        items = []
        if hasattr(obj, 'gallery'):
            for item in obj.gallery.images.values():
                item['url'] = settings.MEDIA_URL + item['file']
                items.append(item)
        return items

    class Meta:
        model = Page
        fields = ('id', 'parent', 'title', 'content', 'content_model', 'slug', 'publish_date',
                  'login_required', 'meta_description', 'tags', 'gallery_items')


class PostCreateSerializer(serializers.ModelSerializer):
    """
    Serializing write access to CREATE a blog post
    """
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True, style={'type': 'textarea'})

    # `categories` field accepts a comma delimited list. Accept blank string to disassociate all categories.
    categories = serializers.CharField(required=False, allow_blank=True)

    # Create a blog post
    def create(self, validated_data):
        # Pop categories attribute to process later
        try:
            categories = validated_data.pop("categories")
        except KeyError:
            categories = None

        # Create a new blog post with core attributes
        initial = {
            "title": validated_data.pop("title"),
            "user": self.context['request'].user,
        }
        post = Post.objects.create(**initial)

        # Update all other object attributes that were supplied in the request (except categories)
        for k, v in validated_data.items():
            setattr(post, k, v)

        # Create categories as necessary from a comma delimited representation and associate them with the blog post
        if categories:
            for name in categories.split(','):
                name = name.strip()
                cat, created = BlogCategory.objects.get_or_create(title=name)
                post.categories.add(cat)

        post.save()

        # Note: response body returned by API on CREATE shows "categories": "blog.BlogCategory.None" rather than
        # the successfully processed comma delimited category list specified in the request.

        return post

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'categories', 'status', 'publish_date', 'expiry_date', 'allow_comments')


class PostUpdateSerializer(serializers.ModelSerializer):
    """
    Serializing write access to UPDATE a blog post
    """
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False, style={'type': 'textarea'})

    # `categories` field accepts a comma delimited list. Accept blank string to disassociate all categories.
    categories = serializers.CharField(required=False, allow_blank=True)

    # Update a blog post
    def update(self, instance, validated_data):
        # Pop categories attribute to process later
        try:
            categories = validated_data.pop("categories")
        except KeyError:
            categories = None

        # Update all object attributes that were supplied in the request (except categories)
        for k, v in validated_data.items():
            setattr(instance, k, v)

        # Handle updating the `categories` field of blog posts using flat representation (comma delimited)
        if categories is not None:
            if categories:
                # Disassociate any blog post categories not included in the request
                cat_titles = [name for name in categories.split(',')]
                for category in instance.categories.all():
                    if category.title not in cat_titles:
                        instance.categories.remove(category)

                # Add any new categories from the request that are not already associated with the blog post
                for name in categories.split(','):
                    name = name.strip()
                    cat, created = BlogCategory.objects.get_or_create(title=name)
                    instance.categories.add(cat)
            else:
                # Categories is an empty string, so disassociate all categories from the blog post
                for category in instance.categories.all():
                    instance.categories.remove(category)

        instance.save()

        return instance

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'categories', 'status', 'publish_date', 'expiry_date', 'allow_comments')


class PostOutputSerializer(serializers.ModelSerializer):
    """
    Serializing read access to blog posts
    """
    user = UserSerializer(required=False, read_only=True)
    categories = CategorySerializer(many=True, required=False, read_only=True)
    tags = serializers.CharField(source='keywords_string', read_only=True)
    short_url = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    excerpt = serializers.SerializerMethodField()

    def get_short_url(self, obj):
        """
        Get short URL of blog post like '/blog/<slug>/' using ``get_absolute_url`` if available.
        Removes dependency on reverse URLs of Mezzanine views when deploying Mezzanine only as an API backend.
        """
        try:
            url = obj.get_absolute_url()
        except NoReverseMatch:
            url = '/blog/' + obj.slug
        return url

    def get_url(self, obj):
        """
        Get full URL of blog post as host + ``get_short_url``, inspired by method ``get_absolute_url_with_host``.
        Removes dependency on reverse URLs of Mezzanine views when deploying Mezzanine only as an API backend.
        """
        return current_request().build_absolute_uri(self.get_short_url(obj))

    def get_excerpt(self, obj):
        """
        Get plain text excerpt of blog post
        """
        return strip_tags(obj.description_from_content())

    class Meta:
        model = Post
        fields = ('id', 'user', 'publish_date', 'updated', 'title', 'content', 'excerpt', 'slug', 'url', 'short_url',
                  'categories', 'allow_comments', 'comments_count', 'comments', 'tags', 'featured_image')
