from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_wishlist', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:wishlist_id>/', views.delete_wishlist, name='delete_wishlist'),
    path('check_wishlist', views.check_wishlist, name='check_wishlist'),
    path('edit_wishlist/<int:wishlist_id>/', views.edit_wishlist, name='edit_wishlist'),
    path('update_wishlist/<int:wishlist_id>/', views.update_wishlist, name='update_wishlist'),
]