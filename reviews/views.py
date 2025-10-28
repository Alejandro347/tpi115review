from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm 
from django.shortcuts import redirect
# Create your views here.

# --- 1. LISTAR (READ - HOMEPAGE) ---
class ReviewList(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'reviews/review_list.html'
    # Las reseñas se ordenan por defecto en el modelo (-created_at)

# --- 2. DETALLE (READ - SEO) ---
class ReviewDetail(DetailView):
    model = Review
    context_object_name = 'review'
    slug_field = 'slug'          # Busca por el campo 'slug' en el modelo
    slug_url_kwarg = 'slug'      # Espera 'slug' en la URL (ej: /reseña/mi-titulo-1/)
    template_name = 'reviews/review_detail.html'

# --- 3. CREAR (CREATE) ---
class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('review_list') 
    template_name = 'reviews/review_form.html'
    
    # Asigna la reseña al usuario logueado antes de guardar
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# --- 4. ACTUALIZAR (UPDATE) ---
class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/review_form.html'

    # Solo el autor puede modificar
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

# --- 5. ELIMINAR (DELETE) ---
class ReviewDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'review'
    success_url = reverse_lazy('review_list')
    template_name = 'reviews/review_confirm_delete.html' 
    
    # Solo el autor puede eliminar
    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user
    
class RegisterPage(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)