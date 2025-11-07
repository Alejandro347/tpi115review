# config/context_processors.py
from django.conf import settings

def seo_context(request):
    """
    Context processor para agregar variables SEO a todos los templates
    """
    return {
        'SITE_URL': settings.SITE_URL,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION,
    }

