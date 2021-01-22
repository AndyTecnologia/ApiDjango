from .models import List, Item
from rest_framework import serializers




class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','done']  

class ListSerializer(serializers.HyperlinkedModelSerializer):

    item_set = ItemSerializer(many=True) #agrega item na lista

    class Meta:
        model = List
        fields = ['id','name','owner','item_set']      

