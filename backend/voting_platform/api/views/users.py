from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import viewsets
from ..models import User
from ..serializers.user import UserSerializer, SignupSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can access this view
    # To allow only admins to create or update users
    # permission_classes = [IsAdminUser]


from authemail.views import Signup

class CustomSignup(Signup):
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer

    @swagger_auto_schema(
        operation_description="User signup endpoint",
        request_body=UserSerializer,
        responses={
            201: openapi.Response("User successfully created", UserSerializer),
            400: "Bad Request",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
