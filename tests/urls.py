from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from mezzanine.core.views import direct_to_template

urlpatterns = i18n_patterns(
    url("^api/", include("mezzanine_api.urls")),

    # Below URLs are required for getting absolute/reverse URLs from Mezzanine views
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url("^", include("mezzanine.urls")),
)
