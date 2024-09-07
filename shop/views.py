from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import permissions, response


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

class ListCarts(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]