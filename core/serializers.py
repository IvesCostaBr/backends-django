from rest_framework import serializers
from .models import List, Item



#oque sera exibido na api
class ItemSeializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'done']


class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSeializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']

