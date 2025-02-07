from rest_framework import generics
from ..models.vote import Vote
from ..serializers.vote_serializer import VoteSerializer

class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer