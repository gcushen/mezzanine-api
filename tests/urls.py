from django.conf.urls import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template


admin.autodiscover()

urlpatterns = patterns(
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    ("^api/", include("mezzanine_api.urls")),
    ("^", include("mezzanine.urls")),
)

handler500 = "mezzanine.core.views.server_error"
