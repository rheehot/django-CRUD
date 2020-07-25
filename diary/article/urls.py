from django.urls import path, include
from article.views import index, create

urlpatterns = [
    path('', index),
    path('create/', create),
]