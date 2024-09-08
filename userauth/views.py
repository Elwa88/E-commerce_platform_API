from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, User
from shop.serializers import Cart, CartSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner = request.user)
        return Response({
            'User': UserSerializer(request.user).data,
            'cart': CartSerializer(cart).data
        })
