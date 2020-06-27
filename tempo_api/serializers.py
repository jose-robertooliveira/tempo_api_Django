from rest_framework import serializers
from .models import Leitura


class LeituraSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leitura
        fields = ['id', 'tempo_leitura', 'temperatura', 'created_on']
