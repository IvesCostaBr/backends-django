from django.shortcuts import render
from rest_framework import viewsets
#from django.shortcuts import HttpResponse
from rest_framework import permissions, authentication
from .models import List, Item
from .serializers import ListSerializer, ItemSeializer

class ListView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user 
        return List.objects.filter(owner=user)


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = Item
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
