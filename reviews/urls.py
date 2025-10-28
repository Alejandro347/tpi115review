# reviews/urls.py
from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate, ReviewUpdate, ReviewDelete

urlpatterns = [
    path('', ReviewList.as_view(), name='review_list'),
    path('crear/', ReviewCreate.as_view(), name='review_create'),
    path('reseña/<slug:slug>/', ReviewDetail.as_view(), name='review_detail'),
    path('editar/<slug:slug>/', ReviewUpdate.as_view(), name='review_update'),
    path('eliminar/<slug:slug>/', ReviewDelete.as_view(), name='review_delete'),
]