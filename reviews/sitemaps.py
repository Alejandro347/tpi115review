# reviews/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Review
from django.urls import reverse
from django.utils import timezone

class ReviewSitemap(Sitemap):
    # Frecuencia con la que esperas que Google rastree esta página
    changefreq = "weekly"
    # Protocolo
    protocol = 'https'

    # 1. Este método le dice a Django qué objetos incluir en el sitemap.
    def items(self):
        # Filtra para excluir reseñas eliminadas o privadas (si existieran)
        return Review.objects.all().order_by('-created_at')
    
    # 2. Este método le dice a Django cómo obtener la URL de cada objeto.
    def location(self, obj):
        return reverse('review_detail', kwargs={'slug': obj.slug})
    
    # 3. Fecha de última modificación (importante para SEO)
    def lastmod(self, obj):
        return obj.created_at
    
    # 4. Prioridad dinámica basada en la antigüedad del contenido
    def priority(self, obj):
        # Reseñas recientes (últimos 30 días) tienen mayor prioridad
        days_old = (timezone.now() - obj.created_at).days
        if days_old < 30:
            return 0.9
        elif days_old < 90:
            return 0.8
        elif days_old < 180:
            return 0.7
        else:
            return 0.6
