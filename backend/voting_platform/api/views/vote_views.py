from rest_framework import generics
from ..models.vote import Votes
from ..serializers.vote_serializer import VotesSerializer

class VoteListCreateView(generics.ListCreateAPIView):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer
