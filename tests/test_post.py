from __future__ import unicode_literals, print_function
from django.core.urlresolvers import reverse
from rest_framework import status
from mezzanine.blog.models import BlogPost as Post
from tests.utils import TestCase


class TestPostViewSet(TestCase):
    """
    Test the API resources for blog posts (read and write)
    """

    def setUp(self):
        """
        Setup the tests
        Create some published and draft blog posts for API retrieval testing
        """
        super(TestPostViewSet, self).setUp()

        # Note for using status:
        # from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
        # status=CONTENT_STATUS_PUBLISHED

        self.post_draft = Post.objects.create(
            title="Draft Post Title",
            content="Draft Content",
            user=self.user)

        self.post_published = Post.objects.create(
            title="Published Post Title",
            content="Published Content",
            publish_date='2016-01-01T00:00',
            user=self.user)

    def tearDown(self):
        """
        Clean up after the tests
        """
        super(TestPostViewSet, self).tearDown()
        self.post_draft.delete()
        self.post_published.delete()

    def test_list_published_posts(self):
        """
        Test API list all published blog posts
        """
        url = reverse('blogpost-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-type'], 'application/json')
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], self.post_published.title)

    def test_retrieve_published_post(self):
        """
        Test API retrieve the published blog post that we created earlier
        """
        url = '/api/posts/{}'.format(self.post_published.pk)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post_published.title)

    def test_retrieve_draft_post(self):
        """
        Test that retrieving a draft post fails since the API only allows read access to published posts
        """
        url = '/api/posts/{}'.format(self.post_draft.pk)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_as_superuser_token(self):
        """
        Test API POST CREATE whilst authenticated via OAuth2 as a superuser
        """
        # Note: we do not directly provide user here, as API should automatically get and
        # authenticate current user as the author
        post_data = {'title': 'title1', 'content': 'content1', 'publish_date': '2016-01-01T00:00',
                     'categories': 'Machine Learning, Statistics'}
        url = '/api/posts'
        response = self.client.post(url, post_data, format='json', HTTP_AUTHORIZATION=self.auth_valid)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.get(pk=response.data['id']).user, self.superuser)
        self.assertEqual(Post.objects.get(pk=response.data['id']).title, post_data['title'])
        self.assertEqual(Post.objects.get(pk=response.data['id']).content, post_data['content'])
        # TODO fix serializer category response
        # self.assertEqual(Post.objects.get(pk=response.data['id']).categories, post_data['categories'])

    def test_create_as_superuser(self):
        """
        Test API POST CREATE whilst authenticated as a superuser
        """
        post_data = {'title': 'title2', 'content': 'content2', 'publish_date': '2016-01-01T00:00',
                     'categories': 'Machine Learning'}
        url = '/api/posts'
        self.client.force_authenticate(user=self.superuser)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.get(pk=response.data['id']).user, self.superuser)
        self.assertEqual(Post.objects.get(pk=response.data['id']).title, post_data['title'])
        self.assertEqual(Post.objects.get(pk=response.data['id']).content, post_data['content'])
        # TODO fix serializer category response
        # self.assertEqual(Post.objects.get(pk=response.data['id']).categories, post_data['categories'])

    def test_create_as_user(self):
        """
        Test API POST CREATE whilst authenticated as a standard user
        """
        post_data = {'title': 'a', 'content': 'b', 'publish_date': '2016-01-01T00:00'}
        url = '/api/posts'
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_as_guest(self):
        """
        Test API POST CREATE whilst unauthenticated as a guest
        """
        post_data = {'title': 'a', 'content': 'b', 'publish_date': '2016-01-01T00:00'}
        url = '/api/posts'
        self.client.force_authenticate(user=None)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_as_superuser_token(self):
        """
        Test API PUT UPDATE whilst authenticated via OAuth2 as a superuser
        """
        # TODO: Add PUT functionality for categories to BlogPost serializer and then test put categories
        put_data = {'title': 'a', 'content': 'b'}
        url = '/api/posts/{}'.format(self.post_published.pk)
        response = self.client.put(url, put_data, format='json', HTTP_AUTHORIZATION=self.auth_valid)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(pk=self.post_published.pk).title, put_data['title'])
        self.assertEqual(Post.objects.get(pk=self.post_published.pk).content, put_data['content'])

    def test_update_as_user(self):
        """
        Test API PUT UPDATE whilst authenticated as a standard user
        """
        put_data = {'title': 'a', 'content': 'b'}
        url = '/api/posts/{}'.format(self.post_published.pk)
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_as_guest(self):
        """
        Test API PUT UPDATE whilst unauthenticated as a guest
        """
        put_data = {'title': 'a', 'content': 'b'}
        url = '/api/posts/{}'.format(self.post_published.pk)
        self.client.force_authenticate(user=None)
        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
