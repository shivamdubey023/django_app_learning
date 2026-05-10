from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop-shop'),
    path('payment/', views.payment, name='shop-payment')
]