
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '0.1',
    'api_path': '/',
    'api_key': '',
    'is_authenticated': False,
    'is_superuser': False,
    'permission_denied_handler': None,
    'info': {
        'title': 'REST API Resource Documentation',
        'description': 'The RESTful web API exposes Mezzanine data using JSON serialization. This interactive document '
                       'will guide you through the relevant data structures, API endpoints, filtering, and searching. '
                       'Bugs should be reported on'
                       ' <a href="https://github.com/gcushen/mezzanine-api/issues" target="_blank">Github</a>.',
    },
    'doc_expansion': 'none',
}
