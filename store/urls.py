from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
]