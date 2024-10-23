from django.urls import path
from .views import *


urlpatterns = [
    path('items-list/', ItemsView.as_view()),
]