import re
from django import http
from rest_framework.reverse import reverse
from mezzanine.conf import settings


class ApiMiddleware(object):
    """Mezzanine API Middleware"""

    def __init__(self, get_response):
        """One-time configuration and initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed by middleware"""
        # Process OPTIONS request
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            return response

        response = self.get_response(request)

        # Add API discovery header for clients
        response['X-Api-Discovery'] = request.build_absolute_uri(reverse('api-root'))

        # Add the CORS headers
        if self.is_api_request(request):
            if settings.MZN_API_CORS_ORIGIN_ALLOW_ALL:
                response['Access-Control-Allow-Origin'] = '*'

            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = ', '.join(settings.MZN_API_CORS_ALLOW_HEADERS)
                response['Access-Control-Allow-Methods'] = ', '.join(settings.MZN_API_CORS_ALLOW_METHODS)

        return response

    def is_api_request(self, request):
        """Returns true if request.path contains the api root URL"""
        return re.match(r'^' + reverse('api-root') + '.*$', request.path)
