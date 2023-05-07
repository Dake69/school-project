from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import heroes
from .serializers import BookSerializer, ItemSerializer, StructuresSerializer, NeutralItemsSerializer, LineCreepsSerializer, SmallCampSerializer, BigCampSerializer, AncientCampSerializer
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import items
from .models import neutral_items
from .models import structures
from .models import line_creeps
from .models import small_neutral_camps
from .models import big_neutral_camps
from .models import ancient_neutral_camps

class HeroViewSet(viewsets.ModelViewSet):
    queryset = heroes.objects.all()
    serializer_class = BookSerializer


class ItemList(viewsets.ModelViewSet):
    queryset = items.objects.all()
    serializer_class = ItemSerializer


class NeutralItemList(viewsets.ModelViewSet):
    queryset = neutral_items.objects.all()
    serializer_class = NeutralItemsSerializer


class Structures(viewsets.ModelViewSet):
    queryset = structures.objects.all()
    serializer_class = StructuresSerializer


class LineCreeps(viewsets.ModelViewSet):
    queryset = line_creeps.objects.all()
    serializer_class = LineCreepsSerializer


class SmallNeutralCamps(viewsets.ModelViewSet):
    queryset = small_neutral_camps.objects.all()
    serializer_class = SmallCampSerializer


class BigNeutralCamps(viewsets.ModelViewSet):
    queryset = big_neutral_camps.objects.all()
    serializer_class = BigCampSerializer


class AncientNeutralCamps(viewsets.ModelViewSet):
    queryset = ancient_neutral_camps.objects.all()
    serializer_class = AncientCampSerializer
