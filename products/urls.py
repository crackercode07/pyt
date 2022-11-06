from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.index),
    path('user/products/', views.products),
    path('signup/', views.signup),
    
]