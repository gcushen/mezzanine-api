from rest_framework.pagination import LimitOffsetPagination
from mezzanine.conf import settings


class MezzaninePagination(LimitOffsetPagination):
    """
    Default pagination class.
    Let large result sets be split into individual pages of data.
    """
    default_limit = 20
    max_limit = getattr(settings, 'MZN_API_LIMIT_MAX', 100)


class PostPagination(MezzaninePagination):
    """
    Pagination for Blog Posts
    """
    default_limit = 10
