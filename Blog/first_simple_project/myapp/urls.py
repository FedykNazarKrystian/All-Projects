from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about123', views.about, name='about'),
    path('contact', views.contact, name='contact')
]
