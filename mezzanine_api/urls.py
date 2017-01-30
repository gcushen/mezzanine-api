from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import UserViewSet, PostViewSet, CategoryViewSet, PageViewSet, SiteViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'pages', PageViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'site', SiteViewSet, SiteViewSet.as_view({'get': 'retrieve'}))

swagger_view = get_swagger_view(title='Mezzanine API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', swagger_view),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
