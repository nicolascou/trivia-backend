from .models import Winner
from rest_framework import viewsets, permissions
from .serializers import WinnerSerializer

class WinnerViewSet(viewsets.ModelViewSet):
    queryset = Winner.objects.all().order_by('-points')
    serializer_class = WinnerSerializer