from rest_framework import generics
from rest_framework.response import Response
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


class NomineesUpdateView(generics.UpdateAPIView):
    """
    Handels HTTP PUT
    """
    queryset = Nominees.objects.all()
    serializer_class = NomineesSerialiser

    def update(self, request, *args, **kwargs):
        """
        Expects one or more values to update in instance
        """
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
