from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, CategoryViewSet, PageViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'pages', PageViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
