"""serializer.py
este archivo nos permitira serializar nuestro modelo de tal manera 
que pueda ser transportado por el protocolo http"""
from rest_framework import serializers
#importamos nuestro modelo a trabajar
from .models import Land

#Esta clase premite tranportar nuestros objetos por la red en formato json
class LandSerializer(serializers.ModelSerializer):
    #Aqui definimos con que modelo vamos a trabajar y los campos
    class Meta:
        model = Land
        fields = '__all__'