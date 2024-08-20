
from django.urls import path
from . import views

urlpatterns = [
    path('', views.songs, name='songs'),
    path('listening/<int:id>', views.listening, name='listening'),
    path('upload/', views.upload, name='upload'),
    path('favorite/', views.favorite, name='favorite'),
    path('add_to_favorite/<int:id>', views.add_to_favorite, name='add_to_favorite'),
    path('remove_from_favorites/<int:id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
