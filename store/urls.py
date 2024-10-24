from django.urls import path
from .views import *


urlpatterns = [
    path('products-list/', ProductsView.as_view()),
]