from .models import List, Item
from rest_framework import serializers




class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name','done']  

class ListSerializer(serializers.HyperlinkedModelSerializer):

    item_set = ItemSerializer(many=True) #agrega item na lista

    class Meta:
        model = List
        fields = ['name','owner','item_set']      

