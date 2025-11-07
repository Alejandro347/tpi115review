# config/context_processors.py
from django.conf import settings

def seo_context(request):
    """
    Context processor para agregar variables SEO a todos los templates
    """
    return {
        'SITE_URL': getattr(settings, 'SITE_URL', 'https://tpi115-review.onrender.com'),
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'TPI115 Review | Opiniones UES'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'Opiniones honestas de la materia TPI115 en la Facultad de Ingeniería y Arquitectura de la Universidad de El Salvador.'),
    }

