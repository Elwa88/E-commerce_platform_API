from django.urls import path
from .views import GetProduct, MyCart, ListProducts, remove_from_cart, order

urlpatterns = [
    path('', ListProducts.as_view()),
    path('add/<int:pk>/', GetProduct.as_view()),
    path('my_cart/<int:owner_id>/', MyCart.as_view()),
    path('my_cart/<int:owner_id>/remove/<int:id>/', remove_from_cart),
    path('order/', order)
]
