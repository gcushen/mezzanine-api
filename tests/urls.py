from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    url("^api/", include("mezzanine_api.urls")),
)
