from rest_framework import generics
from ..models.nominees import Nominees
from ..serializers.nominees_serializer import NomineesSerialiser


class NomineesListCreateView(generics.ListCreateAPIView):
    queryset = Nominees.objects.all()
    serializer_class = NomineesSerialiser

# class NomineesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Nominees.objects.all()
#     serializer_class = NomineesSerialiser
