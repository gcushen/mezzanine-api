from __future__ import unicode_literals, print_function

from rest_framework import status
from rest_framework.test import force_authenticate

from mezzanine.blog.models import BlogCategory
from mezzanine_api.views import CategoryViewSet

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
        self.viewset = CategoryViewSet
        self.category_title = 'Fitness'
        self.category = BlogCategory.objects.create(title=self.category_title)

    def tearDown(self):
        """
        Clean up after the tests
        """
        self.category.delete()

    def test_get_list(self):
        """
        Test API list
        """
        view = self.viewset.as_view({'get': 'list'})
        request = self.factory.get('')
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_get_retrieve(self):
        """
        Test API retrieve
        """
        view = self.viewset.as_view({'get': 'retrieve'})
        request = self.factory.get('')
        response = view(request, pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.category_title)

    def test_post_superuser_token(self):
        """
        Test API POST CREATE whilst authenticated via OAuth2 as a superuser
        """
        post_data_title = 'hello world'
        view = self.viewset.as_view({'post': 'create'})
        request = self.factory.post('', {'title': post_data_title}, format='json', **self.auth_headers)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogCategory.objects.get(pk=response.data['id']).title, post_data_title)

    def test_post_superuser(self):
        """
        Test API POST CREATE whilst authenticated as a superuser
        """
        post_data_title = 'hello world 2'
        view = self.viewset.as_view({'post': 'create'})
        request = self.factory.post('', {'title': post_data_title}, format='json')
        force_authenticate(request, user=self.superuser)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogCategory.objects.get(pk=response.data['id']).title, post_data_title)

    def test_post_user(self):
        """
        Test API POST CREATE whilst authenticated as a standard user
        """
        view = self.viewset.as_view({'post': 'create'})
        request = self.factory.post('', {'title': 'hello world'}, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_guest(self):
        """
        Test API POST CREATE whilst unauthenticated as a guest
        """
        view = self.viewset.as_view({'post': 'create'})
        request = self.factory.post('', {'title': 'hello world'}, format='json')
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_superuser(self):
        """
        Test API PUT UPDATE whilst authenticated as a superuser
        """
        data = 'lol2'
        view = self.viewset.as_view({'put': 'update'})
        request = self.factory.put('', {'title': data}, format='json')
        force_authenticate(request, user=self.superuser)
        response = view(request, pk=int(self.category.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BlogCategory.objects.count(), 1)
        self.assertEqual(BlogCategory.objects.get().title, data)

    def test_put_user(self):
        """
        Test API PUT UPDATE whilst authenticated as a standard user
        """
        data = 'lol2'
        view = self.viewset.as_view({'put': 'update'})
        request = self.factory.put('', {'title': data}, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=int(self.category.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_guest(self):
        """
        Test API PUT UPDATE whilst unauthenticated as a guest
        """
        data = 'lol2'
        view = self.viewset.as_view({'put': 'update'})
        request = self.factory.put('', {'title': data}, format='json')
        response = view(request, pk=int(self.category.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
