from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from ..models.category import Category
from ..serializers.category_serializer import CategorySerializer

class CategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    List all categories or create a new category.
    ---
    parameters:
      - name: name
        type: string
        required: false
        description: Name of the category to filter by
    responses:
      200:
        description: A list of categories
        schema:
          type: array
          items:
            $ref: '#/definitions/Category'
      201:
        description: Category created
        schema:
          $ref: '#/definitions/Category'
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    ordering = ['name']

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a category.
    ---
    responses:
      200:
        description: A single category
        schema:
          $ref: '#/definitions/Category'
      204:
        description: Category deleted
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer