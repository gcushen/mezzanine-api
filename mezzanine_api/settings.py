
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
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
        'title': 'Web API Documentation',
        'description': 'The web API package exposes Mezzanine data through a REST API using JSON serialization. Bugs should be reported on <a href="https://github.com/gcushen/mezzanine-api/issues" target="_blank">Github</a>.',
    },
    'doc_expansion': 'none',
}
