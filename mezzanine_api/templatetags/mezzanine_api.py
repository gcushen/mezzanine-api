from __future__ import unicode_literals
from mezzanine import template
from mezzanine.conf import settings
from .. import __version__

register = template.Library()


@register.simple_tag
def get_mezzanine_api_version():
    return __version__


@register.simple_tag
def get_mezzanine_api_doc_title():
    return settings.MZN_API_DOC_TITLE
