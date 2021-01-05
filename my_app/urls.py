from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:wishlist_id>/', views.delete_wishlist, name='delete_wishlist'),
    path('check_wishlist', views.check_wishlist, name='check_wishlist'),
]