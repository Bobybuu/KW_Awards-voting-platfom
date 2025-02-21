"""
Handels the object-to-json and viseversa converts
"""
from rest_framework import serializers
from ..models.nominees import Nominees
from ..models.category import Category
import uuid


class NomineesSerialiser(serializers.ModelSerializer):
    """
    Handles the serialization process of this table.
    """
    category_id = serializers.CharField()
    class Meta:
        model = Nominees
        fields = ["id", "first_name", "last_name", "bio", "created_at",
                  "updated_at", "image", "votes", "share_link",
                  "category_id", "sub_category"]
        read_only_fields = ["id", "created_at", "votes",]


    def validate_category_id(self, value):
        """
        Validate category ID to handle both UUID and category names.
        """
        try:
            # If value is a valid UUID
            category_uuid = uuid.UUID(value)
            category = Category.objects.get(id=category_uuid)
        except (ValueError, Category.DoesNotExist):
            # Treat value as a category name
            category = Category.objects.filter(name=value).first()
            if not category:
                raise serializers.ValidationError("Invalid Category name"
                                                  +" or UUID")

        # Return the UUID for internal use
        return category

    def create(self, validated_data):
        """
        Creates the object and adds it to the database.
        """
        # Assign the correct UUID from the validated data
        print(validated_data)
        category_id = validated_data.pop("category_id")
        return Nominees.objects.create(category_id=category_id,
                                       **validated_data)

    def validate_name(self, value):
        """
        Makes sure names are unique.
        """
        if Nominees.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError(
                "A nominee with this name exists")
        return value
