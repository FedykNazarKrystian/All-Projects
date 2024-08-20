from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('add_receipts/', views.add_receipts, name='add_receipts'),
    path('edit_receipts/<int:id>', views.edit_receipts, name='edit_receipts'),
    path('receipt/<int:id>', views.receipt, name='receipt'),
]
