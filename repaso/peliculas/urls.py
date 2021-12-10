from rest_framework import routers
from django.urls import path, include

from repaso.peliculas import views

app_name = "peliculas"

router = routers.SimpleRouter()

router.register(r"peliculas", views.PeliculasViewSet, basename="peliculas")

urlpatterns = [
    path('', include(router.urls)),
]
