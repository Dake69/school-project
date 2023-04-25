from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import heroes
from .serializers import BookSerializer
from django.shortcuts import render
from django.http import HttpResponse
from .models import items
from .models import neutral_items


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class BookList(ListAPIView):
    queryset = heroes.objects.all()
    serializer_class = BookSerializer


class ItemList(ListAPIView):
    queryset = items.objects.all()
    serializer_class = BookSerializer

class NeutralItemList(ListAPIView):
    queryset = neutral_items.objects.all()
    serializer_class = BookSerializer
