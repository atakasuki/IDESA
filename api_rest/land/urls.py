"""En este archivo establecemos las rutas de acceso a nuestro Modelo"""

from rest_framework import routers

from .viewsets import LandViewSet

#SimpleRouter define las rutas para nuestro modelo como get post put delete patch para generar nuestra rest_full_api
router = routers.SimpleRouter()

#registramos la url
router.register('land', LandViewSet)

#para registrar las rutas en el proyecto se defire una urlpatterns
urlpatterns = router.urls