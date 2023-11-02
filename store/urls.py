from django.urls import path
from .views import coffee_payment, payment_status
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', coffee_payment, name='coffee-payment'),
    path('payment-status', payment_status, name='payment-status')
    # path('products/', ProductListView.as_view(), name='product_list'),
    # path('products/', views.product_list, name='product_list'),
    # path('product/<slug:product_id>/', views.product_detail, name='product_detail'),
]