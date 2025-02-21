from rest_framework import serializers
from ..models.category import Category
from .sub_category_serializer import SubCategorySerializer

class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'sub_categories']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A category with this name already exists.")
        return value
