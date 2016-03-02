from __future__ import unicode_literals, print_function
from django.core.urlresolvers import reverse
from rest_framework import status
from mezzanine.blog.models import BlogCategory
from tests.utils import TestCase


class TestCategoryViewSet(TestCase):
    """
    Test the API resources for categories
    """

    def setUp(self):
        """
        Setup the tests
        Create a category for API retrieval testing
        """
        super(TestCategoryViewSet, self).setUp()
        self.category = BlogCategory.objects.create(title='Fitness')

    def tearDown(self):
        """
        Clean up after the tests
        """
        self.category.delete()

    def test_list(self):
        """
        Test API list
        """
        url = reverse('blogcategory-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_retrieve(self):
        """
        Test API retrieve
        """
        url = '/api/categories/{}'.format(self.category.pk)
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.category.title)

    def test_create_as_superuser_token(self):
        """
        Test API POST CREATE whilst authenticated via OAuth2 as a superuser
        """
        post_data = {'title': 'my new category 1'}
        url = '/api/categories'
        response = self.client.post(url, post_data, format='json', HTTP_AUTHORIZATION=self.auth_valid)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogCategory.objects.get(pk=response.data['id']).title, post_data['title'])

    def test_create_as_superuser(self):
        """
        Test API POST CREATE whilst authenticated as a superuser
        """
        post_data = {'title': 'my new category 2'}
        url = '/api/categories'
        self.client.force_authenticate(user=self.superuser)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogCategory.objects.get(pk=response.data['id']).title, post_data['title'])

    def test_create_as_user(self):
        """
        Test API POST CREATE whilst authenticated as a standard user
        """
        post_data = {'title': 'my category'}
        url = '/api/categories'
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_as_guest(self):
        """
        Test API POST CREATE whilst unauthenticated as a guest
        """
        post_data = {'title': 'my category'}
        url = '/api/categories'
        self.client.force_authenticate(user=None)
        response = self.client.post(url, post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_as_superuser_token(self):
        """
        Test API PUT UPDATE whilst authenticated via OAuth2 as a superuser
        """
        put_data = {'title': 'my updated category'}
        url = '/api/categories/{}'.format(self.category.pk)
        response = self.client.put(url, put_data, format='json', HTTP_AUTHORIZATION=self.auth_valid)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BlogCategory.objects.get(pk=self.category.pk).title, put_data['title'])

    def test_update_as_user(self):
        """
        Test API PUT UPDATE whilst authenticated as a standard user
        """
        put_data = {'title': 'my updated category'}
        url = '/api/categories/{}'.format(self.category.pk)
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_as_guest(self):
        """
        Test API PUT UPDATE whilst unauthenticated as a guest
        """
        put_data = {'title': 'my updated category'}
        url = '/api/categories/{}'.format(self.category.pk)
        self.client.force_authenticate(user=None)
        response = self.client.put(url, put_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
