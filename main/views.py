from rest_framework.generics import ListAPIView
from rest_framework import generics
from .models import heroes
from .serializers import BookSerializer, ItemSerializer, StructuresSerializer, NeutralItemsSerializer, \
    LineCreepsSerializer, SmallCampSerializer, BigCampSerializer, AncientCampSerializer
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
import mysql.connector
from mysql.connector import Error


def insert_image(image_path):
    try:
        # Открыть соединение с базой данных
        connection = mysql.connector.connect(
            host='localhost',
            database='my_database',
            user='my_user',
            password='my_password'
        )

        # Прочитать данные изображения в бинарном виде
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Вставить данные изображения в таблицу
        cursor = connection.cursor()
        query = "INSERT INTO my_table (image_field) VALUES (%s)"
        cursor.execute(query, (image_data,))
        connection.commit()

        # Закрыть соединение с базой данных
        cursor.close()
        connection.close()

    except Error as e:
        print("Ошибка при работе с базой данных:", e)


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
