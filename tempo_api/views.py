from rest_framework import viewsets
from .serializers import LeituraSerializer
from .models import Leitura


class LeituraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leitura.objects.all()
    serializer_class = LeituraSerializer
