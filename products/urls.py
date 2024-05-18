from django.urls import path
from . import views

urlpatterns = [
     path('',views.products, name = 'products'),
     path('product/<str:name>/', views.product, name='product'),
     path('addProduct',views.addProduct, name = "addProduct"),
     path('updateProduct/<int:pid>/',views.updateProduct, name = "updateProduct"),
     
     
]
