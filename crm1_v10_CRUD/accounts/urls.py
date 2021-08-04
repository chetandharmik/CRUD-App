from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),                 #updated on 21/03/2021 by Chetan Dharmik
    path('products/', views.products, name='products'), #updated on 21/03/2021 by Chetan Dharmik
    path('customer/<str:pk_test>/', views.customer, name="customer"),#updated on 21/03/2021 by Chetan Dharmik

    path('create_order/', views.createOrder, name="create_order"),#updated on 21/03/2021 by Chetan Dharmik
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),#updated on 21/03/2021 by Chetan Dharmik
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),#updated on 21/03/2021 by Chetan Dharmik


]