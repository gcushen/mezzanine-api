from __future__ import unicode_literals, print_function
from django.test import TestCase as BaseTestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory   # , APIClient
from oauth2_provider.models import get_application_model, AccessToken
from django.utils.timezone import now, timedelta


User = get_user_model()
ApplicationModel = get_application_model()


class TestCase(BaseTestCase):
    """
    This is the base test case providing common features for all tests
    """

    def setUp(self):
        """
        Create a request factory for view testing.
        Create a superuser and standard user.
        Create an Oauth2 app for superuser.
        """
        self.factory = APIRequestFactory()
        # self.client = APIClient()

        self.superuser = User.objects.create_superuser('admin', password='admin', email='admin@example.com')
        self.user = User.objects.create_user('test', password='test', email='test@example.com')

        self.app = ApplicationModel.objects.create(
            name='app',
            client_type=ApplicationModel.CLIENT_CONFIDENTIAL,
            authorization_grant_type=ApplicationModel.GRANT_CLIENT_CREDENTIALS,
            user=self.superuser
        )

        self.token = AccessToken.objects.create(user=self.superuser,
                                                token='token_monster',
                                                application=self.app,
                                                expires=now() + timedelta(days=365))

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + 'token_monster',
        }

    def tearDown(self):
        """
        Clean up when tests end
        """
        self.superuser.delete()
        self.user.delete()
        self.app.delete()
        self.token.delete()
