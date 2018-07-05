import re
from django import http
from rest_framework.reverse import reverse
from mezzanine.conf import settings

# Add middleware compatibility for django 1.11 and up.
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class ApiMiddleware(MiddlewareMixin):
    """
    Mezzanine API Middleware
    """

    def process_request(self, request):
        """
        Process OPTIONS request
        """
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            return response
        return None

    def process_response(self, request, response):
        """
        Add the CORS headers and API discovery header for clients
        """
        response['X-Api-Discovery'] = request.build_absolute_uri(reverse('api-root'))

        if self.is_api_request(request):

            if settings.MZN_API_CORS_ORIGIN_ALLOW_ALL:
                response['Access-Control-Allow-Origin'] = '*'

            if request.method == 'OPTIONS':
                response['Access-Control-Allow-Headers'] = ', '.join(settings.MZN_API_CORS_ALLOW_HEADERS)
                response['Access-Control-Allow-Methods'] = ', '.join(settings.MZN_API_CORS_ALLOW_METHODS)

        return response

    def is_api_request(self, request):
        return re.match(r'^' + reverse('api-root') + '.*$', request.path)
