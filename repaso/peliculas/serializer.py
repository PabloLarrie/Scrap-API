from rest_framework import serializers
from repaso.peliculas.models import Pelicula


class PeliculasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pelicula
        fields = [
            "id",
            "Title",
            "Rating",
            "Year",
        ]
