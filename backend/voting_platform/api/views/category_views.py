from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    ordering = ['name']

    @swagger_auto_schema(
        operation_description="List all categories or create a new category",
        responses={
            200: openapi.Response(
                description="A list of categories",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(
                        type=openapi.TYPE_OBJECT, ref='#/definitions/Category'
                    )
                )
            ),
            201: openapi.Response(
                description="Category created",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    ref='#/definitions/Category'
                )
            )
        },
        manual_parameters=[
            openapi.Parameter(
                'name', openapi.IN_QUERY, description="Name of the category to filter by", type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new category",
        request_body=CategorySerializer,
        responses={
            201: openapi.Response(
                description="Category created",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    ref='#/definitions/Category'
                )
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        operation_description="Retrieve a single category by ID",
        responses={
            200: openapi.Response(
                description="Category details",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    ref='#/definitions/Category'
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a category by ID",
        request_body=CategorySerializer,
        responses={
            200: openapi.Response(
                description="Updated category details",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    ref='#/definitions/Category'
                )
            )
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a category by ID",
        responses={204: "Category deleted"}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
