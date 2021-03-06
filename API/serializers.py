from API.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = 'id', 'title', 'description', 'image', 'box_count'
