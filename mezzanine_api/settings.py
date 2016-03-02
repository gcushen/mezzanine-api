REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Requires CSRF token for write access
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

OAUTH2_PROVIDER = {
    # List of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

# API login URL for oauth2_provider (based on default routing in urls.py)
LOGIN_URL = "/api/auth/login/"

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '',
    'api_path': '/',
    'api_key': '',  # Your OAuth2 Access Token
    'token_type': 'Bearer',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'title': 'API Resource Documentation',
        'description': 'The RESTful web API exposes Mezzanine data using JSON serialization and OAuth2 protection. '
                       'This interactive document will guide you through the relevant API endpoints, data structures, '
                       'and query parameters for filtering, searching and pagination. Otherwise, for further '
                       'information and examples, consult the general '
                       '<a href="http://gcushen.github.io/mezzanine-api" target="_blank">Mezzanine API Documentation'
                       '</a>.',
    },
    'doc_expansion': 'none',
}
