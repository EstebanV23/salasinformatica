from rest_framework import viewsets, permissions
from .models import Sala
from .serializaler import SalaSerializer

# Create your views here.

class SalaViewSet(viewsets.ModelViewSet):
  queryset = Sala.objects.all()
  serializer_class = SalaSerializer
  permission_classes = [permissions.AllowAny]
  
# class SalaViewSetOnlySala(viewsets.ModelViewSet):
#   # myid = None
#   # def __init__(self, request):
#   #   self.myid = int(request.GET.get('id'))
  
#   queryset = Sala.objects.get(id=1)
#   serializer_class = SalaSerializer
#   permission_classes = [permissions.AllowAny]