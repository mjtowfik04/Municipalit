from rest_framework import generics
from .serializer import WardSerializer
from .models import Wards

class WorkCreate(generics.ListCreateAPIView):
    queryset=Wards.objects.all()
    serializer_class=WardSerializer
