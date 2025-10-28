# reviews/urls.py
from django.urls import path
from .views import ReviewList, ReviewDetail, ReviewCreate, ReviewUpdate, ReviewDelete

urlpatterns = [
    path('', ReviewList.as_view(), name='review_list'),
    path('crear-opinion/', ReviewCreate.as_view(), name='review_create'),
    path('opinion/<slug:slug>/', ReviewDetail.as_view(), name='review_detail'),
    path('opinion/editar/<slug:slug>/', ReviewUpdate.as_view(), name='review_update'),
    path('opinion/eliminar/<slug:slug>/', ReviewDelete.as_view(), name='review_delete'),
]