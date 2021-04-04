from __future__ import unicode_literals

from API.models import Item
from rest_framework import viewsets, permissions

from django.shortcuts import render
from rest_framework.response import Response
from API.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

