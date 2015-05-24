from __future__ import unicode_literals, print_function

from oauth2_provider.backends import OAuth2Backend
from tests.utils import TestCase


class TestGenerics(TestCase):
    """
    General tests
    """

    def test_authenticate_token(self):
        """
        Test OAuth2 authentication with access token
        """
        request = self.factory.get("/a-resource", **self.auth_headers)
        backend = OAuth2Backend()
        credentials = {'request': request}
        u = backend.authenticate(**credentials)
        self.assertEqual(u, self.superuser)
