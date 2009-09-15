from django.template import Library

register = Library()

def media_url():
    try:
        from django.conf import settings
    except ImportError:
        return ''
    return settings.MEDIA_URL

media_url = register.simple_tag(media_url)