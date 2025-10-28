# reviews/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Review
from django.urls import reverse

class ReviewSitemap(Sitemap):
    # Frecuencia con la que esperas que Google rastree esta página
    changefreq = "weekly"
    # Prioridad (las páginas principales deben tener alta prioridad)
    priority = 0.9

    # 1. Este método le dice a Django qué objetos incluir en el sitemap.
    def items(self):
        # Filtra para excluir reseñas eliminadas o privadas (si existieran)
        return Review.objects.all()
    
    # 2. Este método le dice a Django cómo obtener la URL de cada objeto.
    def location(self, obj):
        return reverse('review_detail', kwargs={'slug': obj.slug})
