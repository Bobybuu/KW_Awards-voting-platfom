from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets
from ..models import User
from ..serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can access this view
    # To allow only admins to create or update users
    # permission_classes = [IsAdminUser]


from authemail.views import Signup
class CustomSignup(Signup):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
