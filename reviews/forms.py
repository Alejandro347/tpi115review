# reviews/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content'] # ¡Solo título y contenido!