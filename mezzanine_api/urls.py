from __future__ import unicode_literals
from django.conf.urls import patterns, url, include
from .views import UserList, UserDetail
from .views import CategoryList, CategoryDetail
from .views import PageList, PageDetail
from .views import PostList, PostDetail

user_urls = patterns('',
    url(r'^/(?P<id>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

category_urls = patterns('',
    url(r'^/(?P<id>[0-9]+)$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^$', CategoryList.as_view(), name='category-list')
)

page_urls = patterns('',
    url(r'^/(?P<id>[0-9]+)$', PageDetail.as_view(), name='page-detail'),
    url(r'^$', PageList.as_view(), name='page-list')
)

post_urls = patterns('',
    url(r'^/(?P<id>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
    url(r'^categories', include(category_urls)),
    url(r'^pages', include(page_urls)),
    url(r'^posts', include(post_urls)),
    url("^", include('rest_framework_swagger.urls')),
)
