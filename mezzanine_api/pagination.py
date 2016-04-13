from rest_framework.pagination import PageNumberPagination
from mezzanine.conf import settings


class MezzaninePagination(PageNumberPagination):
    """
    Default pagination class.
    Let large result sets be split into individual pages of data.
    """
    page_size = 20
    page_size_query_param = 'per_page'
    max_page_size = getattr(settings, 'MZN_API_MAX_PER_PAGE', 100)


class PostPagination(MezzaninePagination):
    """
    Pagination for Blog Posts
    """
    page_size = 10
