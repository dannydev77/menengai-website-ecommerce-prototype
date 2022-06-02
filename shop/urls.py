from django.urls import path 
from . import views
urlpatterns = [
 path('store/', views.store, name='store'),
 path('cart/', views.cart, name='cart'),
 path('checkout/', views.checkout, name='checkout'),
 path('update/', views.update_item, name='update'),
 path('detail/<slug:slug>', views.detail, name='detail'),
 path('delete/<slug:slug>', views.delete_item, name='delete'),

]