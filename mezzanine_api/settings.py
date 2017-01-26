# Default REST API settings
# This module should be imported into your Django `settings.py`
# Edit your `local_settings.py` to customize

from django.core.urlresolvers import reverse_lazy


allow_headers = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
)

MZN_API_CORS_ORIGIN_ALLOW_ALL = True
MZN_API_CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
MZN_API_CORS_ALLOW_HEADERS = allow_headers
MZN_API_DOC_TITLE = "API Resource Documentation"
MZN_API_DOC_INTRO = """
The RESTful web API exposes Mezzanine data using JSON serialization and OAuth2 protection.
This interactive document will guide you through the relevant API endpoints, data structures,
and query parameters for filtering, searching and pagination.
Otherwise, for general information and examples, consult the
<a href="http://gcushen.github.io/mezzanine-api" target="_blank">Mezzanine API Documentation</a>.
The <a href="http://gcushen.github.io/mezzanine-api/client/" target="_blank">API Client SDK</a> and
<a href="../oauth2/applications/">OAuth App Manager</a> are available for app development.
"""

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read access',
        'write': 'Write access',
    },
    'ACCESS_TOKEN_EXPIRE_SECONDS': 1209600,  # 2 weeks
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 3600,  # 1 hour
}

# Django login URL required for authentication with oauth2_provider package
LOGIN_URL = reverse_lazy('rest_framework:login')

SWAGGER_SETTINGS = {
    'api_version': '',
    'api_path': '/',
    'api_key': '',  # Your OAuth2 Access Token
    'token_type': 'Bearer',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'title': MZN_API_DOC_TITLE,
        'description': MZN_API_DOC_INTRO,
    },
    'doc_expansion': 'none',
}

ENGAGEMENT_MANAGER_ID="id2"