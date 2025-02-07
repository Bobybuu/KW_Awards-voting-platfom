"""
Handels the object-to-json and viseversa converts
"""
from rest_framework import generics
from rest_framework.response import Response
from ..models.awards import Awards
from ..serializers.awards_serializer import AwardsSerializer

class AwardsListCreateView(generics.ListCreateAPIView):
    """
    Handels HTTP GET and POST
    """
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer


class AwardsDeleteView(generics.DestroyAPIView):
    """
    Handels HTTP DELETE
    """
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer


class AwardsUpdateView(generics.UpdateAPIView):
    """
    Handels HTTP PUT
    """
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer

    def update(self, request, *args, **kwargs):
        """
        Expects one or more values to update in instance
        """
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
