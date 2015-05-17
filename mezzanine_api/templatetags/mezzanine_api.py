from __future__ import unicode_literals
from mezzanine import template
from .. import __version__

register = template.Library()


@register.simple_tag
def get_mezzanine_api_version():
    return __version__
