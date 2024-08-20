from django.urls import path, include
from . import views
from myapp.views import contact


urlpatterns = [
    path('newsapp', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add_news', views.add_news, name='add_news'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path("logout/", views.user_logout, name='logout'),
    path('edit_news/<int:id>/', views.edit_news, name='edit_news'),
    path('contact/', contact, name='contacts')
]
