from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .models import Venda, Item
from .serializers import VendaSerializer, ItemSerializer
# Create your views here.


#as views que vao ser executadas quando entrar no endpoint
class VendaView(viewsets.ModelViewSet):

    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]