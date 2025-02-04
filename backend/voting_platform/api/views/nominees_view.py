from rest_framework import generics
from ..models.nominees import Nominees
from ..serializers.nominees_serializer import NomineesSerialiser


class NomineesListCreateView(generics.ListCreateAPIView):
    """
    Handels HTTP GET and POST
    """
    queryset = Nominees.objects.all()
    serializer_class = NomineesSerialiser


class NomineesDeleteView(generics.DestroyAPIView):
    """
    Handels HTTP DELETE
    """
    queryset = Nominees.objects.all()
    serializer_class = NomineesSerialiser
