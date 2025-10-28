# reviews/models.py
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify 
from django.urls import reverse

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    # El slug ahora se basa en el título + el usuario (para asegurar unicidad si dos títulos son iguales)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.user.username}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']