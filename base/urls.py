from django.urls import path 
from . import views
urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('products/', views.products, name='products'),
 path('product/', views.product, name='product'),
 path('contact/', views.contact, name='contact'),
 path('management/', views.users, name='management'),
 path('careers/', views.careers, name='careers')
]