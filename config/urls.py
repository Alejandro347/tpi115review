"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from reviews.sitemaps import ReviewSitemap
from reviews.views import RegisterPage

sitemaps = {
    'reviews': ReviewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # RUTA PARA SERVIR ROBOTS.TXT
    path('robots.txt', 
         TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    
    # 1. URLS DE LA APP PRINCIPAL: DEBE IR PRIMERO (para que ReviewList maneje la raíz '/')
    path('', include('reviews.urls')), 
    
    # 2. URLS DE AUTENTICACIÓN: DEBE IR DESPUÉS
    path('', include('django.contrib.auth.urls')), 
    
    # 3. URL del Sitemap (SEO)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # 4. URL DE REGISTRO DE USUARIOS
    path('register/', RegisterPage.as_view(), name='register'),
]
