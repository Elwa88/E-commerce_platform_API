from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import permissions, response
from django.shortcuts import HttpResponse

class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProducts(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class CreateCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class GetProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):

        cart, created = Cart.objects.get_or_create(owner = request.user)
        product = self.get_object()
        cart.product.add(product)

        return response.Response({
            'message': 'Product added to cart',
            'product': ProductSerializer(product).data
        })

class MyCart(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'owner_id'
    permission_classes = [permissions.IsAuthenticated]

def remove_from_cart(request,owner_id,id):
    cart = Cart.objects.get(owner_id=owner_id)
    products = cart.product.all()
    product_name = products[id].name
    cart.product.remove(products[id])
    return HttpResponse(f'{product_name} has been removed from cart')


def order(request):
    cart = Cart.objects.get(owner = request.user)
    products = cart.product.all()
    total = 0
    for product in products:
        total += product.price
        cart.product.remove(product)
    return HttpResponse(f'Congratulations on your purchase. The total payment is {total}$. Your cart has been cleared')