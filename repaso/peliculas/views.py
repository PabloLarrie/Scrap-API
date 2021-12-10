from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from repaso.peliculas.models import Pelicula
from repaso.peliculas.serializer import PeliculasSerializer


class PeliculasViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Pelicula.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["Title", "Rating", "Year"]
    ordering = ("id",)

    def get_serializer_class(self):
        return PeliculasSerializer
