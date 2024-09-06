from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export_reading_csv, name='export_reading_csv'),
]
