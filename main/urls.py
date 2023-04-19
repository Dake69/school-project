from django.urls import path
from . import views
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
urlpatterns = [
    path('', views.index),
    path('about', views.about)
]