from django.urls import path
from . import views

urlpatterns = [
     path('',views.products, name = 'products'),
     path('product/<str:name>/', views.product, name='product'),
     
]
