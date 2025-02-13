from rest_framework import serializers
from ..models.sub_category import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'category_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_name(self, value):
        if SubCategory.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A sub category with this name already exists.")
        return value
