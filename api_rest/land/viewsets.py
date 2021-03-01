"""Por medio de este archivo podremos realizar un CRUD sobre nuestro objetos de nuestros modelos"""
from rest_framework import viewsets
from .models import Land
from .serializer import LandSerializer
class LandViewSet(viewsets.ModelViewSet):
    queryset =  Land.objects.all().filter()
    serializer_class = LandSerializer