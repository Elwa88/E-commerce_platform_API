from django.urls import path
from .views import GetProduct, ListCarts, ListProducts

urlpatterns = [
    path('', ListProducts.as_view()),
    path('add/<int:pk>/', GetProduct.as_view()),
    path('my_cart', ListCarts.as_view())
]
