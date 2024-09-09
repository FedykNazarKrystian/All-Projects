from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('private_data/', views.private_data, name='private_data'),
    path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
]
