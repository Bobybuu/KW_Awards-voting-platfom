"""
Handels the object-to-json and viseversa converts
"""
from rest_framework import generics
from ..models.awards import Awards
from ..serializers.awards_serializer import AwardsSerializer

class AwardsListCreateView(generics.ListCreateAPIView):
    """
    Handels HTTP GET and POST
    """
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
