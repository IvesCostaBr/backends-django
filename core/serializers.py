from rest_framework import serializers
from .models import Venda, Item



#oque sera exibido na api
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        felds = ['id' ,'nome_items']
        exclude = ['venda']


class VendaSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = Venda
        fields = ('id' ,'owner', 'code', 'status', 'url', 'item_set')

