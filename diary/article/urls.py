from django.urls import path, include
from article.views import index, create, retrieve, update, delete

app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('create/', create, name='create'),
    path('article/<int:pk>', retrieve, name='retrieve'),
    path('update/<int:pk>', update, name='update'),
    path('article/<int:pk>/delete/', delete, name='delete')
]